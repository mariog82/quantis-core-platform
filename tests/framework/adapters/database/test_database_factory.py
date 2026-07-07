from framework.adapters import AdapterContext
from framework.adapters.database.factory import create_in_memory_database_adapter


def test_create_in_memory_database_adapter():
    adapter = create_in_memory_database_adapter(AdapterContext(tenant_id="tenant-demo"))

    assert adapter.context.tenant_id == "tenant-demo"
    assert adapter.connected is True
