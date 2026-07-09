from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class RepositoryTreeEntry:
    path: str
    is_dir: bool
    size_bytes: int = 0


@dataclass(frozen=True)
class RepositoryAuditIssue:
    code: str
    path: str
    message: str


@dataclass
class RepositoryAuditReport:
    root: Path
    tree: list[RepositoryTreeEntry] = field(default_factory=list)
    issues: list[RepositoryAuditIssue] = field(default_factory=list)
    total_files: int = 0
    total_directories: int = 0
    total_python_files: int = 0

    @property
    def passed(self) -> bool:
        return not self.issues

    def add_issue(self, code: str, path: str, message: str) -> None:
        self.issues.append(RepositoryAuditIssue(code, path, message))

    def to_markdown(self) -> str:
        return (
            "# Repository Audit Report\n\n"
            f"Status: `{'PASS' if self.passed else 'WARN'}`\n\n"
            f"- Files: `{self.total_files}`\n"
            f"- Python files: `{self.total_python_files}`\n"
        )


RepositoryTreeEntry.__test__ = False
RepositoryAuditIssue.__test__ = False
RepositoryAuditReport.__test__ = False


def run_repository_audit(root: Path | str = ".") -> RepositoryAuditReport:
    repo_root = Path(root).resolve()
    report = RepositoryAuditReport(root=repo_root)

    for path in repo_root.rglob("*"):
        if ".git" in path.parts or "__pycache__" in path.parts:
            continue

        if path.is_dir():
            report.total_directories += 1
            report.tree.append(RepositoryTreeEntry(path=path.relative_to(repo_root).as_posix(), is_dir=True))
            continue

        report.total_files += 1
        if path.suffix == ".py":
            report.total_python_files += 1
        report.tree.append(RepositoryTreeEntry(path=path.relative_to(repo_root).as_posix(), is_dir=False, size_bytes=path.stat().st_size))

    return report
