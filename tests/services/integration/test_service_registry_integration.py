from services.registry import create_default_enterprise_services


def test_default_enterprise_service_registry_contains_all_services():
    registry = create_default_enterprise_services()

    assert registry.exists("licensing")
    assert registry.exists("subscription")
    assert registry.exists("billing")
    assert registry.exists("provisioning")
    assert registry.exists("compliance")


def test_all_default_enterprise_services_are_healthy():
    registry = create_default_enterprise_services()

    results = [service.health() for service in registry.list_services()]

    assert all(result.success for result in results)
