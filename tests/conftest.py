"""Global pytest path guard."""

from pathlib import Path
import sys


def pytest_configure() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    repo_root_str = str(repo_root)
    shadow_path = str(repo_root / "tests" / "framework" / "adapters")

    sys.path[:] = [
        path
        for path in sys.path
        if str(path).rstrip("\\/") != shadow_path.rstrip("\\/")
    ]

    if repo_root_str in sys.path:
        sys.path.remove(repo_root_str)
    sys.path.insert(0, repo_root_str)
