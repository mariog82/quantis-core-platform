from framework.contracts.module import BaseModule, ModuleManifest
from framework.runtime import RuntimeKernel, RuntimeManager, RuntimeState


class KernelModule(BaseModule):
    manifest = ModuleManifest(name="kernel-demo", version="0.1.0")

    def __init__(self):
        self.started = False

    def boot(self):
        pass

    def start(self):
        self.started = True

    def stop(self):
        self.started = False

    def shutdown(self):
        pass


def test_kernel_start_stop():
    manager = RuntimeManager()
    module = KernelModule()
    manager.register(module)

    kernel = RuntimeKernel(manager)
    kernel.boot()
    kernel.initialize()

    assert kernel.start() == RuntimeState.RUNNING
    assert module.started is True
    assert kernel.stop() == RuntimeState.STOPPED
