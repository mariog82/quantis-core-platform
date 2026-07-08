from sdk import QuantisClient, SDKConfig

def test_quantis_client_health():
    client = QuantisClient(SDKConfig(base_url="http://localhost:8000"))
    response = client.health()
    assert response.success is True
    assert response.data["status"] == "ok"

def test_quantis_client_resource_registry():
    client = QuantisClient()
    client.register_resource("tenants/demo", {"tenant_id": "demo"})
    response = client.get_resource("tenants/demo")
    assert response.success is True
    assert response.data["tenant_id"] == "demo"

def test_quantis_client_missing_resource():
    client = QuantisClient()
    response = client.get_resource("missing")
    assert response.success is False
    assert response.error == "RESOURCE_NOT_FOUND"
