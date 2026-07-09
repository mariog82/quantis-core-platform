from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class CIGate:
    name: str
    command: str


@dataclass(frozen=True)
class CIStabilizationIssue:
    code: str
    path: str
    message: str


@dataclass
class CIStabilizationReport:
    root: Path
    issues: list[CIStabilizationIssue] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.issues

    def add_issue(self, code: str, path: str, message: str) -> None:
        self.issues.append(CIStabilizationIssue(code, path, message))

    def to_markdown(self) -> str:
        lines = ["# CI Stabilization Report", "", f"Status: `{'PASS' if self.passed else 'FAIL'}`", ""]
        for issue in self.issues:
            lines.append(f"- `{issue.code}` — `{issue.path}` — {issue.message}")
        return "\n".join(lines)


CIGate.__test__ = False
CIStabilizationIssue.__test__ = False
CIStabilizationReport.__test__ = False


def run_ci_stabilization_checks(root: Path | str = ".") -> CIStabilizationReport:
    repo_root = Path(root).resolve()
    report = CIStabilizationReport(root=repo_root)
    workflow = repo_root / ".github/workflows/ci.yml"

    if not workflow.exists():
        report.add_issue("MISSING_WORKFLOW", ".github/workflows/ci.yml", "Required CI workflow is missing.")
        return report

    content = workflow.read_text(encoding="utf-8")
    for pattern in ["ruff", "pytest"]:
        if pattern not in content:
            report.add_issue("MISSING_CI_PATTERN", ".github/workflows/ci.yml", f"Required CI pattern `{pattern}` is missing.")

    return report
