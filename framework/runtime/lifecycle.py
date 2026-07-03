from framework.contracts.module import BaseModule
from framework.runtime.context import RuntimeContext
from framework.runtime.state import ModuleState


class ModuleLifecycleManager:
    def initialize(self, module: BaseModule, context: RuntimeContext | None = None) -> ModuleState:
        if hasattr(module, "initialize"):
            module.initialize(context)
        return ModuleState.INITIALIZED

    def boot(self, module: BaseModule) -> ModuleState:
        module.boot()
        return ModuleState.READY

    def start(self, module: BaseModule) -> ModuleState:
        if hasattr(module, "start"):
            module.start()
        return ModuleState.RUNNING

    def stop(self, module: BaseModule) -> ModuleState:
        if hasattr(module, "stop"):
            module.stop()
        else:
            module.shutdown()
        return ModuleState.STOPPED

    def dispose(self, module: BaseModule) -> ModuleState:
        if hasattr(module, "dispose"):
            module.dispose()
        return ModuleState.STOPPED

    def restart(self, module: BaseModule, context: RuntimeContext | None = None) -> ModuleState:
        self.stop(module)
        self.initialize(module, context)
        self.boot(module)
        return self.start(module)
