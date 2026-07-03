from framework.runtime.events import KernelStarted, KernelStopped
from framework.runtime.health import RuntimeHealth
from framework.runtime.manager import RuntimeManager
from framework.runtime.state import RuntimeState


class RuntimeKernel:
    def __init__(self, manager: RuntimeManager | None = None):
        self.manager = manager or RuntimeManager()
        self.state = RuntimeState.STOPPED

    def boot(self) -> RuntimeState:
        self.state = RuntimeState.BOOTING
        return self.state

    def initialize(self) -> RuntimeState:
        self.state = RuntimeState.INITIALIZING
        self.manager.initialize_all()
        return self.state

    def start(self) -> RuntimeState:
        self.manager.start_all()
        self.state = RuntimeState.RUNNING
        self.manager.events.append(KernelStarted())
        return self.state

    def reload(self) -> RuntimeState:
        self.stop()
        self.boot()
        self.initialize()
        return self.start()

    def stop(self) -> RuntimeState:
        self.state = RuntimeState.STOPPING
        self.manager.stop_all()
        self.state = RuntimeState.STOPPED
        self.manager.events.append(KernelStopped())
        return self.state

    def shutdown(self) -> RuntimeState:
        return self.stop()

    def status(self) -> dict:
        modules = []
        for module in self.manager.registry.list_modules():
            name = module.manifest.name
            modules.append({"name": name, "state": self.manager.registry.state(name).value})
        return {"state": self.state.value, "modules": modules}

    def health(self) -> RuntimeHealth:
        reports = self.manager.registry.health()
        if not reports:
            return RuntimeHealth.READY
        if any(report.status.value == "FAILED" for report in reports):
            return RuntimeHealth.FAILED
        if any(report.status.value == "UNKNOWN" for report in reports):
            return RuntimeHealth.PARTIAL
        return RuntimeHealth.READY
