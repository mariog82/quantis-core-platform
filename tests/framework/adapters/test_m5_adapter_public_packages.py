import importlib

PACKAGES = ["framework.adapters", "framework.adapters.sdk", "sdk", "sdk.generator"]

def test_m5_adapter_and_sdk_packages_define_all():
    for package_name in PACKAGES:
        module = importlib.import_module(package_name)
        assert hasattr(module, "__all__")
        assert module.__all__
