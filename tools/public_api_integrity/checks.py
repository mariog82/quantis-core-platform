from importlib import import_module
from pathlib import Path


def run_public_api_integrity_checks(root: Path | str = "."):
    issues = []
    for package in ["framework.adapters", "sdk", "sdk.generator"]:
        try:
            module = import_module(package)
        except Exception as exc:
            issues.append(f"{package}: {exc}")
            continue
        if not hasattr(module, "__all__"):
            issues.append(f"{package}: missing __all__")
    return issues
