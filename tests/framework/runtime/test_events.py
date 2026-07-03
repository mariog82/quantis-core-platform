from framework.runtime.events import (
    KernelStarted,
    KernelStopped,
    ModuleRegistered,
    ModuleStarted,
    ModuleStopped,
)


def test_module_registered_event():
    event = ModuleRegistered(module="analytics")

    assert event.module == "analytics"


def test_module_started_event():
    event = ModuleStarted(module="reporting")

    assert event.module == "reporting"


def test_kernel_events():
    started = KernelStarted(module="kernel")
    stopped = KernelStopped(module="kernel")

    assert started.module == "kernel"
    assert stopped.module == "kernel"