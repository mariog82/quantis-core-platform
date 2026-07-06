from typing import Callable

from framework.adapters.adapter import Adapter
from framework.adapters.context import AdapterContext
from framework.adapters.exceptions import AdapterNotFound


AdapterBuilder = Callable[[AdapterContext], Adapter]


class AdapterFactory:
    def __init__(self):
        self._builders: dict[str, AdapterBuilder] = {}

    def register_builder(self, name: str, builder: AdapterBuilder) -> None:
        self._builders[name] = builder

    def create(self, name: str, context: AdapterContext | None = None) -> Adapter:
        context = context or AdapterContext()
        if name not in self._builders:
            raise AdapterNotFound(name)

        adapter = self._builders[name](context)
        adapter.configure(context)
        return adapter
