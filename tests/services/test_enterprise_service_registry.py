from services.registry import create_default_enterprise_services


def test_default_enterprise_services_registry():
    registry = create_default_enterprise_services()

    assert registry.exists("licensing")
    assert registry.exists("subscription")
    assert registry.exists("billing")
    assert registry.exists("provisioning")
    assert registry.exists("compliance")
