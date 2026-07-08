import importlib


PUBLIC_PACKAGES = [
    "framework.adapters",
    "framework.adapters.ai",
    "framework.adapters.auth",
    "framework.adapters.database",
    "framework.adapters.http",
    "framework.adapters.identity",
    "framework.adapters.messaging",
    "framework.adapters.notification",
    "framework.adapters.payment",
    "framework.adapters.sdk",
    "framework.adapters.storage",
    "sdk",
    "sdk.generator",
]


def test_m5_public_packages_are_importable_and_define_all():
    for package_name in PUBLIC_PACKAGES:
        module = importlib.import_module(package_name)
        assert hasattr(module, "__all__")
        assert module.__all__
