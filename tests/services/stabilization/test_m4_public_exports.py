import importlib


PUBLIC_SERVICE_PACKAGES = [
    "services.licensing",
    "services.subscription",
    "services.billing",
    "services.provisioning",
    "services.compliance",
]


def test_service_packages_define_all():
    for package_name in PUBLIC_SERVICE_PACKAGES:
        module = importlib.import_module(package_name)
        assert hasattr(module, "__all__")
        assert module.__all__
