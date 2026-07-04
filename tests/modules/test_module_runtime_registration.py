from framework.runtime import RuntimeKernel, RuntimeManager, RuntimeState
from modules.registry import register_default_modules


def test_register_default_modules_in_runtime():
    manager = RuntimeManager()
    register_default_modules(manager)

    assert manager.registry.exists("analytics")
    assert manager.registry.exists("reporting")
    assert manager.registry.exists("dashboard")
    assert manager.registry.exists("notification")


def test_default_modules_start_with_runtime():
    manager = RuntimeManager()
    register_default_modules(manager)

    kernel = RuntimeKernel(manager)
    kernel.boot()
    kernel.initialize()

    assert kernel.start() == RuntimeState.RUNNING
    assert manager.registry.get("analytics").started is True
    assert manager.registry.get("reporting").started is True
