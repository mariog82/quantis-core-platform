import importlib


PUBLIC_PACKAGES = [
    "framework.runtime",
    "framework.di",
    "framework.persistence",
    "framework.api",
    "framework.plugins",
    "framework.workflow",
    "framework.dashboard",
    "framework.reporting",
]


def test_public_framework_packages_importable():
    for package_name in PUBLIC_PACKAGES:
        module = importlib.import_module(package_name)
        assert module is not None


def test_public_framework_packages_define_all():
    for package_name in PUBLIC_PACKAGES:
        module = importlib.import_module(package_name)
        assert hasattr(module, "__all__")
        assert isinstance(module.__all__, list)
        assert module.__all__
