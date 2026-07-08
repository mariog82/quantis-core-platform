import importlib
import sys
from pathlib import Path


PUBLIC_PACKAGES = [
    "framework.adapters",
    "framework.adapters.http",
    "framework.adapters.database",
    "framework.adapters.auth",
    "framework.adapters.storage",
    "framework.adapters.messaging",
    "framework.adapters.ai",
    "framework.adapters.notification",
    "framework.adapters.payment",
    "framework.adapters.identity",
    "framework.adapters.sdk",
    "sdk",
    "sdk.generator",
]


def _ensure_repo_root_first() -> None:
    repo_root = Path(__file__).resolve().parents[4]
    repo_root_str = str(repo_root)

    if repo_root_str in sys.path:
        sys.path.remove(repo_root_str)

    sys.path.insert(0, repo_root_str)

    loaded_sdk = sys.modules.get("sdk")
    if loaded_sdk is not None:
        loaded_sdk_file = getattr(loaded_sdk, "__file__", "") or ""
        if "\\tests\\framework\\adapters\\sdk\\" in loaded_sdk_file:
            sys.modules.pop("sdk", None)
            sys.modules.pop("sdk.generator", None)


def test_m5_public_packages_are_importable_and_define_all():
    _ensure_repo_root_first()

    for package_name in PUBLIC_PACKAGES:
        module = importlib.import_module(package_name)

        assert hasattr(module, "__all__")
        assert module.__all__
