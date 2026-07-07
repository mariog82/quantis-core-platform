from framework.adapters import AdapterContext
from framework.adapters.auth.factory import create_in_memory_authentication_adapter


def test_create_in_memory_authentication_adapter_configures_context():
    adapter = create_in_memory_authentication_adapter(
        AdapterContext(tenant_id="tenant-demo")
    )

    assert adapter.context.tenant_id == "tenant-demo"
