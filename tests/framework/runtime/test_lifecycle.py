from framework.contracts.module import BaseModule, ModuleManifest
from framework.runtime import ModuleLifecycleManager, ModuleState


class LifecycleModule(BaseModule):
    manifest = ModuleManifest(name="lifecycle", version="0.1.0")

    def __init__(self):
        self.calls = []

    def initialize(self, context):
        self.calls.append("initialize")

    def boot(self):
        self.calls.append("boot")

    def start(self):
        self.calls.append("start")

    def stop(self):
        self.calls.append("stop")

    def shutdown(self):
        self.calls.append("shutdown")


def test_lifecycle_manager():
    module = LifecycleModule()
    lifecycle = ModuleLifecycleManager()

    assert lifecycle.initialize(module) == ModuleState.INITIALIZED
    assert lifecycle.boot(module) == ModuleState.READY
    assert lifecycle.start(module) == ModuleState.RUNNING
    assert lifecycle.stop(module) == ModuleState.STOPPED
    assert module.calls == ["initialize", "boot", "start", "stop"]
