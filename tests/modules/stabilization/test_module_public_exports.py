import importlib


PUBLIC_MODULE_PACKAGES = [
    "modules.analytics",
    "modules.reporting",
    "modules.dashboard",
    "modules.notification",
]


def test_module_packages_define_all():
    for package_name in PUBLIC_MODULE_PACKAGES:
        module = importlib.import_module(package_name)
        assert hasattr(module, "__all__")
        assert module.__all__
