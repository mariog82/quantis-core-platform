from dataclasses import dataclass, field
from typing import Any

from framework.plugins.exceptions import ExtensionPointNotFound


@dataclass
class ExtensionPoint:
    name: str
    description: str = ""
    metadata: dict = field(default_factory=dict)
    handlers: list[Any] = field(default_factory=list)

    def add_handler(self, handler: Any) -> None:
        self.handlers.append(handler)


class ExtensionPointRegistry:
    def __init__(self):
        self._items: dict[str, ExtensionPoint] = {}

    def register(self, extension_point: ExtensionPoint) -> ExtensionPoint:
        self._items[extension_point.name] = extension_point
        return extension_point

    def get(self, name: str) -> ExtensionPoint:
        if name not in self._items:
            raise ExtensionPointNotFound(name)
        return self._items[name]

    def exists(self, name: str) -> bool:
        return name in self._items

    def list(self) -> list[ExtensionPoint]:
        return list(self._items.values())

    def attach(self, name: str, handler: Any) -> None:
        self.get(name).add_handler(handler)
