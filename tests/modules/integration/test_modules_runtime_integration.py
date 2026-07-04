from framework.runtime import RuntimeKernel, RuntimeManager, RuntimeState
from modules.registry import register_default_modules


def test_default_modules_register_and_start_in_runtime():
    manager = RuntimeManager()
    register_default_modules(manager)

    kernel = RuntimeKernel(manager)
    kernel.boot()
    kernel.initialize()

    assert kernel.start() == RuntimeState.RUNNING

    assert manager.registry.exists("analytics")
    assert manager.registry.exists("reporting")
    assert manager.registry.exists("dashboard")
    assert manager.registry.exists("notification")

    assert manager.registry.get("analytics").started is True
    assert manager.registry.get("reporting").started is True
    assert manager.registry.get("dashboard").started is True
    assert manager.registry.get("notification").started is True
