from dataclasses import dataclass, field
from pathlib import Path


IGNORED_DIRS = {
    ".git",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
}

SOURCE_SUFFIXES = {".py", ".md", ".yml", ".yaml", ".toml", ".txt"}


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
        self.issues.append(RepositoryAuditIssue(code=code, path=path, message=message))

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


def _collect_tree(root: Path, report: RepositoryAuditReport) -> None:
    for path in sorted(root.rglob("*")):
        rel = _relative(root, path)
        if _ignored(Path(rel)):
            continue

        if path.is_dir():
            report.total_directories += 1
            report.tree.append(RepositoryTreeEntry(path=rel, is_dir=True))
            continue

        report.total_files += 1
        if path.suffix == ".py":
            report.total_python_files += 1
        report.tree.append(
            RepositoryTreeEntry(
                path=rel,
                is_dir=False,
                size_bytes=path.stat().st_size,
            )
        )


def _detect_pycache_only_dirs(root: Path, report: RepositoryAuditReport) -> None:
    for path in root.rglob("*"):
        if not path.is_dir() or _ignored(path.relative_to(root)):
            continue
        children = [child.name for child in path.iterdir()]
        if children == ["__pycache__"]:
            report.add_issue(
                "PYCACHE_ONLY_DIRECTORY",
                _relative(root, path),
                "Directory contains only __pycache__.",
            )


def _detect_empty_python_packages(root: Path, report: RepositoryAuditReport) -> None:
    for init_file in root.rglob("__init__.py"):
        if _ignored(init_file.relative_to(root)):
            continue
        package_dir = init_file.parent
        python_files = [path for path in package_dir.glob("*.py") if path.name != "__init__.py"]
        child_packages = [
            path
            for path in package_dir.iterdir()
            if path.is_dir() and (path / "__init__.py").exists()
        ]
        if not python_files and not child_packages and package_dir.name not in {"tests"}:
            # This is a warning, not a failure condition.
            report.add_issue(
                "EMPTY_PACKAGE",
                _relative(root, package_dir),
                "Package has only __init__.py and no child packages.",
            )


def _detect_large_generated_files(root: Path, report: RepositoryAuditReport) -> None:
    for path in root.rglob("*"):
        if not path.is_file() or _ignored(path.relative_to(root)):
            continue
        if path.suffix in SOURCE_SUFFIXES and path.stat().st_size > 500_000:
            report.add_issue(
                "LARGE_SOURCE_FILE",
                _relative(root, path),
                "Source-like file is larger than 500KB.",
            )


def run_repository_audit(root: Path | str = ".") -> RepositoryAuditReport:
    repo_root = Path(root).resolve()
    report = RepositoryAuditReport(root=repo_root)

    _collect_tree(repo_root, report)
    _detect_pycache_only_dirs(repo_root, report)
    _detect_empty_python_packages(repo_root, report)
    _detect_large_generated_files(repo_root, report)

    return report
