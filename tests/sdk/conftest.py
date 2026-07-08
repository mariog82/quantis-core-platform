"""Ensure tests/sdk imports the application SDK package, not adapter tests/sdk."""

from pathlib import Path
import sys


def pytest_configure() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    repo_root_str = str(repo_root)

    if repo_root_str in sys.path:
        sys.path.remove(repo_root_str)

    sys.path.insert(0, repo_root_str)

    for module_name in list(sys.modules):
        if module_name == "sdk" or module_name.startswith("sdk."):
            module = sys.modules.get(module_name)
            module_file = getattr(module, "__file__", "") or ""
            normalized = module_file.replace("/", "\\")

            if "\\tests\\framework\\adapters\\sdk\\" in normalized:
                sys.modules.pop(module_name, None)
