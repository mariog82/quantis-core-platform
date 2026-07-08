from framework.adapters.sdk import InMemorySDKAdapter, SDKCallRequest

def test_in_memory_sdk_adapter_calls_registered_operation():
    adapter = InMemorySDKAdapter()
    adapter.register_operation("health", {"status": "ok"})
    response = adapter.call(SDKCallRequest(operation="health"))
    assert response.success is True
    assert response.data["status"] == "ok"

def test_sdk_adapter_execute_call_operation():
    adapter = InMemorySDKAdapter()
    adapter.register_operation("health", {"status": "ok"})
    result = adapter.execute("call", {"request": SDKCallRequest(operation="health")})
    assert result.success is True
    assert result.data.success is True
