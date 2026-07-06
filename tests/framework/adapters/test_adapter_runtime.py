from framework.adapters import AdapterContext
from framework.adapters.runtime import AdapterRuntime
from framework.adapters.testing import EchoAdapter


def test_adapter_runtime_executes_adapter():
    runtime = AdapterRuntime()
    runtime.register(EchoAdapter(), AdapterContext(tenant_id="tenant-demo"))
    runtime.start_all()

    result = runtime.execute("echo", "echo", {"message": "hello"})

    assert result.success is True
    assert result.data == {"message": "hello"}

    runtime.stop_all()
    assert runtime.registry.get("echo").state.value == "stopped"
