import importlib


PACKAGES = [
    "framework.adapters",
    "framework.adapters.http",
    "framework.adapters.database",
    "framework.adapters.auth",
    "framework.adapters.storage",
    "framework.adapters.messaging",
    "framework.adapters.ai",
    "framework.adapters.notification",
]


def test_m5_adapter_packages_define_all():
    for package_name in PACKAGES:
        module = importlib.import_module(package_name)
        assert hasattr(module, "__all__")
        assert module.__all__
