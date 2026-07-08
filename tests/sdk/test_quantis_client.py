from sdk import QuantisClient


def test_quantis_client_health():
    response = QuantisClient().health()

    assert response.data["status"] == "ok"


def test_quantis_client_resource_registry():
    client = QuantisClient()
    client.register_resource("x", {"ok": True})

    response = client.get_resource("x")

    assert response.data["ok"] is True
