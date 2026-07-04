from __future__ import annotations

from framework.contracts.plugin import BasePlugin
from framework.plugins.exceptions import PluginAlreadyRegistered, PluginNotFound


class PluginRegistry:
    def __init__(self):
        self._plugins: dict[str, BasePlugin] = {}

    def register(self, plugin: BasePlugin) -> BasePlugin:
        name = plugin.manifest.name
        if name in self._plugins:
            raise PluginAlreadyRegistered(name)
        self._plugins[name] = plugin
        return plugin

    def unregister(self, name: str) -> None:
        if name not in self._plugins:
            raise PluginNotFound(name)
        self._plugins.pop(name)

    def get(self, name: str) -> BasePlugin:
        if name not in self._plugins:
            raise PluginNotFound(name)
        return self._plugins[name]

    def exists(self, name: str) -> bool:
        return name in self._plugins

    def list_plugins(self) -> list[BasePlugin]:
        return list(self._plugins.values())

    def list(self) -> list[BasePlugin]:
        return self.list_plugins()

    def enabled(self) -> list[BasePlugin]:
        return [plugin for plugin in self._plugins.values() if plugin.status == "enabled"]
