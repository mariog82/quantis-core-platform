from pathlib import Path
import shutil


def run_repository_recovery(root: Path | str = "."):
    repo_root = Path(root).resolve()
    removed = []
    for path in list(repo_root.rglob("__pycache__")):
        if ".git" in path.parts:
            continue
        shutil.rmtree(path, ignore_errors=True)
        removed.append(path.relative_to(repo_root).as_posix())
    return removed
