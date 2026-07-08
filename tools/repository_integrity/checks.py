from dataclasses import dataclass, field
from pathlib import Path


PUBLIC_PACKAGES = [
    "framework",
    "framework/adapters",
    "framework/adapters/http",
    "framework/adapters/database",
    "framework/adapters/auth",
    "framework/adapters/storage",
    "framework/adapters/messaging",
    "framework/adapters/ai",
    "framework/adapters/notification",
    "framework/adapters/payment",
    "framework/adapters/identity",
    "framework/adapters/sdk",
    "sdk",
    "sdk/generator",
]

REQUIRED_FILES = [
    "VERSION",
    "README.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "docs/release/M5_BETA_FREEZE.md",
]


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
        lines = [
            "# Repository Integrity Report",
            "",
            f"Root: `{self.root}`",
            f"Status: `{'PASS' if self.passed else 'FAIL'}`",
            "",
        ]
        if self.passed:
            lines.append("No repository integrity issues found.")
            return "\n".join(lines)

        lines.extend(["## Issues", ""])
        for issue in self.issues:
            lines.append(f"- `{issue.code}` — `{issue.path}` — {issue.message}")
        return "\n".join(lines)


RepositoryIntegrityIssue.__test__ = False
RepositoryIntegrityReport.__test__ = False


def _is_namespace_package(path: Path) -> bool:
    return path.is_dir() and not (path / "__init__.py").exists()


def _contains_only_pycache(path: Path) -> bool:
    if not path.is_dir():
        return False
    return [child.name for child in path.iterdir()] == ["__pycache__"]


def run_repository_integrity_checks(root: Path | str = ".") -> RepositoryIntegrityReport:
    repo_root = Path(root).resolve()
    report = RepositoryIntegrityReport(root=repo_root)

    for package in PUBLIC_PACKAGES:
        package_path = repo_root / package
        if not package_path.exists():
            report.add_issue("MISSING_PACKAGE", package, "Required public package directory is missing.")
            continue
        if _is_namespace_package(package_path):
            report.add_issue("MISSING_INIT", package, "Package is missing __init__.py.")
        if _contains_only_pycache(package_path):
            report.add_issue("PYCACHE_ONLY_PACKAGE", package, "Package contains only __pycache__.")

    for required_file in REQUIRED_FILES:
        if not (repo_root / required_file).exists():
            report.add_issue("MISSING_REQUIRED_FILE", required_file, "Required repository file is missing.")

    return report
