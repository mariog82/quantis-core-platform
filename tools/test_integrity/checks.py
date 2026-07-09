from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class IntegrityIssue:
    code: str
    path: str
    message: str


@dataclass
class IntegrityReport:
    root: Path
    issues: list[IntegrityIssue] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.issues

    def add_issue(self, code: str, path: str, message: str) -> None:
        self.issues.append(IntegrityIssue(code, path, message))

    def to_markdown(self) -> str:
        lines = ["# Test Integrity Report", "", f"Status: `{'PASS' if self.passed else 'FAIL'}`", ""]
        for issue in self.issues:
            lines.append(f"- `{issue.code}` — `{issue.path}` — {issue.message}")
        return "\n".join(lines)


IntegrityIssue.__test__ = False
IntegrityReport.__test__ = False
TestIntegrityIssue = IntegrityIssue
TestIntegrityReport = IntegrityReport
TestIntegrityIssue.__test__ = False
TestIntegrityReport.__test__ = False


def _contains_only_pycache(path: Path) -> bool:
    return path.is_dir() and [child.name for child in path.iterdir()] == ["__pycache__"]


def run_test_integrity_checks(root: Path | str = ".") -> IntegrityReport:
    repo_root = Path(root).resolve()
    report = IntegrityReport(root=repo_root)

    for directory in ["tests", "tests/sdk", "tests/framework/adapters/stabilization"]:
        path = repo_root / directory
        if not path.exists():
            report.add_issue("MISSING_TEST_DIRECTORY", directory, "Expected test directory is missing.")
            continue
        if _contains_only_pycache(path):
            report.add_issue("PYCACHE_ONLY_TEST_DIRECTORY", directory, "Test directory contains only __pycache__.")

    return report
