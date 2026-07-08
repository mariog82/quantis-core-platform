from dataclasses import dataclass, field
from pathlib import Path


TEST_DIRECTORIES = [
    "tests/core",
    "tests/framework",
    "tests/framework/adapters",
    "tests/framework/adapters/stabilization",
    "tests/modules",
    "tests/services",
    "tests/sdk",
    "tests/tools",
]

PUBLIC_SOURCE_TO_TEST_DIR = {
    "framework/adapters": "tests/framework/adapters",
    "sdk": "tests/sdk",
    "tools/repository_integrity": "tests/tools/repository_integrity",
}


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
        self.issues.append(IntegrityIssue(code=code, path=path, message=message))

    def to_markdown(self) -> str:
        lines = [
            "# Test Integrity Report",
            "",
            f"Root: `{self.root}`",
            f"Status: `{'PASS' if self.passed else 'FAIL'}`",
            "",
        ]

        if self.passed:
            lines.append("No test integrity issues found.")
            return "\n".join(lines)

        lines.append("## Issues")
        lines.append("")
        for issue in self.issues:
            lines.append(f"- `{issue.code}` — `{issue.path}` — {issue.message}")

        return "\n".join(lines)


IntegrityIssue.__test__ = False
IntegrityReport.__test__ = False

# Backward-compatible public aliases.
TestIntegrityIssue = IntegrityIssue
TestIntegrityReport = IntegrityReport
TestIntegrityIssue.__test__ = False
TestIntegrityReport.__test__ = False


def _has_test_files(path: Path) -> bool:
    return path.is_dir() and any(path.glob("test_*.py"))


def _contains_only_pycache(path: Path) -> bool:
    if not path.is_dir():
        return False
    children = [child.name for child in path.iterdir()]
    return children == ["__pycache__"]


def _has_python_files(path: Path) -> bool:
    return path.is_dir() and any(path.rglob("*.py"))


def run_test_integrity_checks(root: Path | str = ".") -> IntegrityReport:
    repo_root = Path(root).resolve()
    report = IntegrityReport(root=repo_root)

    for directory in TEST_DIRECTORIES:
        test_dir = repo_root / directory

        if not test_dir.exists():
            report.add_issue(
                "MISSING_TEST_DIRECTORY",
                directory,
                "Expected test directory is missing.",
            )
            continue

        if _contains_only_pycache(test_dir):
            report.add_issue(
                "PYCACHE_ONLY_TEST_DIRECTORY",
                directory,
                "Test directory contains only __pycache__.",
            )
            continue

        if not _has_python_files(test_dir):
            report.add_issue(
                "EMPTY_TEST_DIRECTORY",
                directory,
                "Test directory has no Python files.",
            )

    for source_dir, test_dir in PUBLIC_SOURCE_TO_TEST_DIR.items():
        source_path = repo_root / source_dir
        target_test_path = repo_root / test_dir

        if source_path.exists() and not _has_test_files(target_test_path):
            report.add_issue(
                "MISSING_TEST_FILES",
                test_dir,
                f"Public source directory `{source_dir}` has no test_*.py files in `{test_dir}`.",
            )

    return report
