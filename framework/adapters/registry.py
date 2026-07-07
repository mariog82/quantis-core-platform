from framework.adapters.adapter import Adapter
from framework.adapters.exceptions import AdapterAlreadyRegistered, AdapterNotFound


class AdapterRegistry:
    def __init__(self):
        self._adapters: dict[str, Adapter] = {}

    def register(self, adapter: Adapter) -> Adapter:
        name = adapter.metadata.name
        if name in self._adapters:
            raise AdapterAlreadyRegistered(name)
        self._adapters[name] = adapter
        return adapter

    def get(self, name: str) -> Adapter:
        if name not in self._adapters:
            raise AdapterNotFound(name)
        return self._adapters[name]

    def exists(self, name: str) -> bool:
        return name in self._adapters

    def list_adapters(self) -> list[Adapter]:
        return list(self._adapters.values())

    def find_by_type(self, adapter_type: str) -> list[Adapter]:
        return [
            adapter
            for adapter in self._adapters.values()
            if adapter.metadata.adapter_type == adapter_type
        ]

    def find_by_capability(self, capability: str) -> list[Adapter]:
        return [
            adapter
            for adapter in self._adapters.values()
            if capability in adapter.metadata.capabilities
        ]
