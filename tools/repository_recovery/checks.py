from dataclasses import dataclass, field
from pathlib import Path
import shutil


@dataclass
class CleanupResult:
    removed: list[str] = field(default_factory=list)

    @property
    def count(self) -> int:
        return len(self.removed)


def find_pycache_only_directories(root: Path | str = ".") -> list[Path]:
    repo_root = Path(root).resolve()
    result: list[Path] = []

    for path in repo_root.rglob("*"):
        if not path.is_dir():
            continue
        if ".git" in path.parts:
            continue
        if [child.name for child in path.iterdir()] == ["__pycache__"]:
            result.append(path)

    return result


def remove_pycache_only_directories(root: Path | str = ".") -> CleanupResult:
    repo_root = Path(root).resolve()
    result = CleanupResult()

    for path in find_pycache_only_directories(repo_root):
        relative = path.relative_to(repo_root).as_posix()
        shutil.rmtree(path)
        result.removed.append(relative)

    return result


def run_repository_recovery(root: Path | str = ".") -> list[str]:
    return remove_pycache_only_directories(root).removed