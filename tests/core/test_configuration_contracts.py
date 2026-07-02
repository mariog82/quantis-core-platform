from core.configuration import ConfigurationService

def test_platform_configuration_get_set():
    service = ConfigurationService()
    service.set("app.name", "Quantis")
    assert service.get("app.name") == "Quantis"

def test_tenant_configuration_overrides_platform():
    service = ConfigurationService()
    service.set("feature.analytics", False)
    service.set("feature.analytics", True, scope="tenant", tenant_id="tenant-1")
    assert service.get("feature.analytics", tenant_id="tenant-1") is True
    assert service.get("feature.analytics", tenant_id="tenant-2") is False

def test_default_value():
    service = ConfigurationService()
    assert service.get("missing", default="fallback") == "fallback"
