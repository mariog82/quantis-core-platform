from framework.adapters import AdapterContext
from framework.adapters.sdk.factory import create_in_memory_sdk_adapter

def test_create_in_memory_sdk_adapter_configures_context():
    adapter = create_in_memory_sdk_adapter(AdapterContext(tenant_id="tenant-demo"))
    assert adapter.context.tenant_id == "tenant-demo"
