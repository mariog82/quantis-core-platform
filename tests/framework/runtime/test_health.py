from framework.contracts.module import BaseModule, ModuleManifest
from framework.runtime import ModuleHealth, ModuleRegistry, RuntimeHealth, RuntimeKernel, RuntimeManager


class HealthyModule(BaseModule):
    manifest = ModuleManifest(name="healthy", version="0.1.0")

    def boot(self):
        pass

    def shutdown(self):
        pass


def test_registry_health_unknown_before_running():
    registry = ModuleRegistry()
    registry.register(HealthyModule())

    report = registry.health()[0]

    assert report.status == ModuleHealth.UNKNOWN


def test_kernel_health_ready_without_modules():
    assert RuntimeKernel(RuntimeManager()).health() == RuntimeHealth.READY
