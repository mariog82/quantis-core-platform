from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class RepositoryIntegrityIssue:
    code: str
    path: str
    message: str


@dataclass
class RepositoryIntegrityReport:
    root: Path
    issues: list[RepositoryIntegrityIssue] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.issues

    def add_issue(self, code: str, path: str, message: str) -> None:
        self.issues.append(RepositoryIntegrityIssue(code, path, message))

    def to_markdown(self) -> str:
        lines = ["# Repository Integrity Report", "", f"Status: `{'PASS' if self.passed else 'FAIL'}`", ""]
        for issue in self.issues:
            lines.append(f"- `{issue.code}` — `{issue.path}` — {issue.message}")
        return "\n".join(lines)


RepositoryIntegrityIssue.__test__ = False
RepositoryIntegrityReport.__test__ = False


def run_repository_integrity_checks(root: Path | str = ".") -> RepositoryIntegrityReport:
    repo_root = Path(root).resolve()
    report = RepositoryIntegrityReport(root=repo_root)

    public_packages = [
        "framework",
        "framework/adapters",
        "sdk",
        "sdk/generator",
        "tools/repository_integrity",
        "tools/test_integrity",
        "tools/public_api_integrity",
        "tools/ci_stabilization",
        "tools/release_manager",
        "tools/repository_audit",
        "tools/repository_recovery",
    ]

    for package in public_packages:
        path = repo_root / package
        if not path.exists():
            report.add_issue("MISSING_PACKAGE", package, "Required package directory is missing.")
            continue
        if not (path / "__init__.py").exists():
            report.add_issue("MISSING_INIT", package, "Package is missing __init__.py.")

    return report
