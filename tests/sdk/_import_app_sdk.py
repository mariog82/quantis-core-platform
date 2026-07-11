"""Helpers to import the real application SDK during pytest collection.

Pytest may temporarily put `tests/framework/adapters` before the repository
root on sys.path. In that case, `import sdk` resolves to
`tests/framework/adapters/sdk` instead of the real application package `sdk`.

These helpers force repository root precedence and remove the shadowing path
before importing the application SDK package.
"""

from pathlib import Path
import importlib
import sys


def import_app_sdk():
    repo_root = Path(__file__).resolve().parents[2]
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

    for module_name in list(sys.modules):
        if module_name == "sdk" or module_name.startswith("sdk."):
            module = sys.modules.get(module_name)
            module_file = getattr(module, "__file__", "") or ""
            normalized = module_file.replace("/", "\\")
            if "\\tests\\framework\\adapters\\sdk\\" in normalized:
                sys.modules.pop(module_name, None)

    return importlib.import_module("sdk")


def import_app_sdk_generator():
    import_app_sdk()
    return importlib.import_module("sdk.generator")
