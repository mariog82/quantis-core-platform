from framework.adapters import AdapterContext
from framework.adapters.ai.factory import create_in_memory_ai_adapter

def test_create_in_memory_ai_adapter_configures_context():
    adapter = create_in_memory_ai_adapter(AdapterContext(tenant_id="tenant-demo"))
    assert adapter.context.tenant_id == "tenant-demo"
