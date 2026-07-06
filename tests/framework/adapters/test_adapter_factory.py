from framework.adapters import AdapterContext, AdapterFactory
from framework.adapters.testing import EchoAdapter


def test_adapter_factory_creates_and_configures_adapter():
    factory = AdapterFactory()
    factory.register_builder("echo", lambda context: EchoAdapter())

    adapter = factory.create("echo", AdapterContext(tenant_id="tenant-demo"))

    assert adapter.context.tenant_id == "tenant-demo"
