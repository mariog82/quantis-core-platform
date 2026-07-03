from framework.contracts.module import BaseModule
from framework.runtime.context import RuntimeContext
from framework.runtime.dependency_graph import DependencyGraph
from framework.runtime.events import ModuleInitialized, ModuleRegistered, ModuleStarted, ModuleStopped, RuntimeEvent
from framework.runtime.lifecycle import ModuleLifecycleManager
from framework.runtime.registry import ModuleRegistry
from framework.runtime.state import ModuleState

class RuntimeManager:
    def __init__(self, context: RuntimeContext | None = None, registry: ModuleRegistry | None = None, lifecycle: ModuleLifecycleManager | None = None, dependency_graph: DependencyGraph | None = None):
        self.context = context or RuntimeContext()
        self.registry = registry or ModuleRegistry()
        self.lifecycle = lifecycle or ModuleLifecycleManager()
        self.dependency_graph = dependency_graph or DependencyGraph()
        self.events: list[RuntimeEvent] = []

    def register(self, module: BaseModule) -> BaseModule:
        registered = self.registry.register(module)
        self.dependency_graph.add(module.manifest.name, getattr(module.manifest, 'dependencies', []))
        self.events.append(ModuleRegistered(module.manifest.name))
        return registered

    def initialize_all(self) -> None:
        for name in self.dependency_graph.sort():
            module = self.registry.get(name)
            self.registry.set_state(name, self.lifecycle.initialize(module, self.context))
            self.events.append(ModuleInitialized(name))

    def start_all(self) -> None:
        for name in self.dependency_graph.sort():
            module = self.registry.get(name)
            self.registry.set_state(name, self.lifecycle.boot(module))
            self.registry.set_state(name, self.lifecycle.start(module))
            self.events.append(ModuleStarted(name))

    def stop_all(self) -> None:
        for module in reversed(self.registry.list()):
            name = module.manifest.name
            self.registry.set_state(name, ModuleState.STOPPING)
            self.registry.set_state(name, self.lifecycle.stop(module))
            self.events.append(ModuleStopped(name))
