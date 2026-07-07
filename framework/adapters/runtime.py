from framework.adapters.adapter import Adapter
from framework.adapters.context import AdapterContext
from framework.adapters.registry import AdapterRegistry
from framework.adapters.result import AdapterResult

class AdapterRuntime:
    def __init__(self, registry: AdapterRegistry | None = None):
        self.registry = registry or AdapterRegistry()

    def register(self, adapter: Adapter, context: AdapterContext | None = None) -> Adapter:
        if context is not None:
            adapter.configure(context)
        self.registry.register(adapter)
        return adapter

    def start_all(self) -> None:
        for adapter in self.registry.list_adapters():
            adapter.start()

    def stop_all(self) -> None:
        for adapter in self.registry.list_adapters():
            adapter.stop()

    def execute(self, adapter_name: str, operation: str, payload: dict | None = None) -> AdapterResult:
        adapter = self.registry.get(adapter_name)
        return adapter.execute(operation, payload or {})
