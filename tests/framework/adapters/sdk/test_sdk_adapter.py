from framework.adapters.sdk import InMemorySDKAdapter, SDKCallRequest


def test_sdk_adapter_call():
    adapter = InMemorySDKAdapter()
    adapter.register_operation("health", {"status": "ok"})

    response = adapter.call(SDKCallRequest("health"))

    assert response.data["status"] == "ok"
