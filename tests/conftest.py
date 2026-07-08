"""Pytest import-path guard for repository-local packages."""

from pathlib import Path
import sys


def _ensure_repo_root_first() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    repo_root_str = str(repo_root)

    if repo_root_str in sys.path:
        sys.path.remove(repo_root_str)

    sys.path.insert(0, repo_root_str)


def _drop_shadowed_sdk_modules() -> None:
    for module_name in list(sys.modules):
        if not (module_name == "sdk" or module_name.startswith("sdk.")):
            continue

        module = sys.modules.get(module_name)
        module_file = getattr(module, "__file__", "") or ""
        normalized = module_file.replace("/", "\\")

        if "\\tests\\framework\\adapters\\sdk\\" in normalized:
            sys.modules.pop(module_name, None)


_ensure_repo_root_first()
_drop_shadowed_sdk_modules()
