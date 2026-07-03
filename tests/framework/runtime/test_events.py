from framework.runtime.events import KernelStarted, ModuleRegistered, ModuleStarted, ModuleStopped


def test_kernel_started_event():
    event = KernelStarted()

    assert event.event_type == "kernel.started"


def test_module_registered_event():
    event = ModuleRegistered("analytics")

    assert event.event_type == "module.registered"
    assert event.module_name == "analytics"


def test_module_started_event():
    event = ModuleStarted("analytics")

    assert event.event_type == "module.started"
    assert event.module_name == "analytics"


def test_module_stopped_event():
    event = ModuleStopped("analytics")

    assert event.event_type == "module.stopped"
    assert event.module_name == "analytics"
