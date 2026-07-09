from pathlib import Path


def run_repository_integrity_checks(root: Path | str = "."):
    repo_root = Path(root).resolve()
    required = ["VERSION", "README.md", "CHANGELOG.md", "ROADMAP.md", "sdk/__init__.py", "framework/__init__.py"]
    return [path for path in required if not (repo_root / path).exists()]
