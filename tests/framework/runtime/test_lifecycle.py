from framework.contracts import ModuleManifest
from framework.runtime.lifecycle import LifecycleManager
from framework.runtime.state import ModuleState


class DemoModule:
    manifest = ModuleManifest(name="demo", version="0.1.0")
    state = ModuleState.CREATED


def test_initialize_module():
    module = DemoModule()
    lifecycle = LifecycleManager()

    lifecycle.initialize(module)

    assert module.state == ModuleState.INITIALIZED


def test_start_module():
    module = DemoModule()
    lifecycle = LifecycleManager()

    lifecycle.start(module)

    assert module.state == ModuleState.RUNNING


def test_stop_module():
    module = DemoModule()
    lifecycle = LifecycleManager()

    lifecycle.stop(module)

    assert module.state == ModuleState.STOPPED