from dataclasses import dataclass, field
from pathlib import Path


IGNORED_DIRS = {".git", ".pytest_cache", ".mypy_cache", ".ruff_cache", "__pycache__", ".venv", "venv", "node_modules", "dist", "build"}
PLACEHOLDER_PACKAGES = {"sdk/python", "sdk/typescript"}


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
        return not any(issue.code in {"PYCACHE_ONLY_DIRECTORY", "LARGE_SOURCE_FILE"} for issue in self.issues)

    def add_issue(self, code: str, path: str, message: str) -> None:
        self.issues.append(RepositoryAuditIssue(code, path, message))

    def to_markdown(self) -> str:
        lines = [
            "# Repository Audit Report",
            "",
            f"Root: `{self.root}`",
            f"Status: `{'PASS' if self.passed else 'WARN'}`",
            "",
            "## Summary",
            "",
            f"- Total files: `{self.total_files}`",
            f"- Total directories: `{self.total_directories}`",
            f"- Python files: `{self.total_python_files}`",
            "",
        ]
        if self.issues:
            lines.extend(["## Issues", ""])
            for issue in self.issues:
                lines.append(f"- `{issue.code}` — `{issue.path}` — {issue.message}")
            lines.append("")

        lines.extend(["## Repository Tree", ""])
        for entry in self.tree[:500]:
            marker = "📁" if entry.is_dir else "📄"
            lines.append(f"- {marker} `{entry.path}`")

        if len(self.tree) > 500:
            lines.append(f"- ... truncated, total entries: {len(self.tree)}")
        return "\n".join(lines)


RepositoryTreeEntry.__test__ = False
RepositoryAuditIssue.__test__ = False
RepositoryAuditReport.__test__ = False


def _ignored(path: Path) -> bool:
    return any(part in IGNORED_DIRS for part in path.parts)


def _relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def run_repository_audit(root: Path | str = ".") -> RepositoryAuditReport:
    repo_root = Path(root).resolve()
    report = RepositoryAuditReport(root=repo_root)

    for path in sorted(repo_root.rglob("*")):
        rel_path = path.relative_to(repo_root)
        if _ignored(rel_path):
            continue

        rel = rel_path.as_posix()
        if path.is_dir():
            report.total_directories += 1
            report.tree.append(RepositoryTreeEntry(path=rel, is_dir=True))

            children = [child.name for child in path.iterdir()]
            if children == ["__pycache__"]:
                report.add_issue("PYCACHE_ONLY_DIRECTORY", rel, "Directory contains only __pycache__.")
            continue

        report.total_files += 1
        if path.suffix == ".py":
            report.total_python_files += 1

        if path.suffix in {".py", ".md", ".yml", ".yaml", ".toml", ".txt"} and path.stat().st_size > 500_000:
            report.add_issue("LARGE_SOURCE_FILE", rel, "Source-like file is larger than 500KB.")

        report.tree.append(RepositoryTreeEntry(path=rel, is_dir=False, size_bytes=path.stat().st_size))

    for init_file in repo_root.rglob("__init__.py"):
        rel_dir = init_file.parent.relative_to(repo_root).as_posix()
        if rel_dir in PLACEHOLDER_PACKAGES or _ignored(init_file.relative_to(repo_root)):
            continue

    return report
