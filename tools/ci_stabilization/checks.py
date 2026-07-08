from dataclasses import dataclass, field
from pathlib import Path


REQUIRED_WORKFLOWS = [
    ".github/workflows/ci.yml",
]

REQUIRED_PATTERNS = [
    "ruff",
    "pytest",
    "tools.repository_integrity.cli",
    "tools.test_integrity.cli",
    "tools.public_api_integrity.cli",
]


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
        lines = [
            "# CI Stabilization Report",
            "",
            f"Root: `{self.root}`",
            f"Status: `{'PASS' if self.passed else 'FAIL'}`",
            "",
        ]
        if self.passed:
            lines.append("No CI stabilization issues found.")
            return "\n".join(lines)

        lines.extend(["## Issues", ""])
        for issue in self.issues:
            lines.append(f"- `{issue.code}` — `{issue.path}` — {issue.message}")
        return "\n".join(lines)


CIGate.__test__ = False
CIStabilizationIssue.__test__ = False
CIStabilizationReport.__test__ = False


def _workflow_missing_required_patterns(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    return [pattern for pattern in REQUIRED_PATTERNS if pattern not in content]


def run_ci_stabilization_checks(root: Path | str = ".") -> CIStabilizationReport:
    repo_root = Path(root).resolve()
    report = CIStabilizationReport(root=repo_root)

    for workflow in REQUIRED_WORKFLOWS:
        workflow_path = repo_root / workflow
        if not workflow_path.exists():
            report.add_issue("MISSING_WORKFLOW", workflow, "Required CI workflow is missing.")
            continue

        for pattern in _workflow_missing_required_patterns(workflow_path):
            report.add_issue("MISSING_CI_PATTERN", workflow, f"Required CI pattern `{pattern}` is missing.")

    return report
