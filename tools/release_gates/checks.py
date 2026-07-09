from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class ReleaseGateIssue:
    code: str
    path: str
    message: str


@dataclass
class ReleaseGateReport:
    root: Path
    issues: list[ReleaseGateIssue] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.issues

    def add_issue(self, code: str, path: str, message: str) -> None:
        self.issues.append(ReleaseGateIssue(code, path, message))

    def to_markdown(self) -> str:
        lines = ["# Release Gates Report", "", f"Status: `{'PASS' if self.passed else 'FAIL'}`", ""]
        for issue in self.issues:
            lines.append(f"- `{issue.code}` — `{issue.path}` — {issue.message}")
        return "\n".join(lines)


ReleaseGateIssue.__test__ = False
ReleaseGateReport.__test__ = False


def run_release_gate_checks(root: Path | str = ".") -> ReleaseGateReport:
    repo_root = Path(root).resolve()
    report = ReleaseGateReport(root=repo_root)

    current_dir = repo_root / "tests/release/current"
    history_dir = repo_root / "tests/release/history"

    if not current_dir.exists():
        report.add_issue("MISSING_CURRENT_RELEASE_GATES", "tests/release/current", "Current release gate directory is missing.")
    elif not any(current_dir.glob("test_*.py")):
        report.add_issue("EMPTY_CURRENT_RELEASE_GATES", "tests/release/current", "Current release gate directory has no test_*.py files.")

    if not history_dir.exists():
        report.add_issue("MISSING_HISTORICAL_RELEASE_GATES", "tests/release/history", "Historical release gate directory is missing.")

    return report
