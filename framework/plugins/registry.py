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

    def get(self, name: str) -> BasePlugin:
        if name not in self._plugins:
            raise PluginNotFound(name)
        return self._plugins[name]

    def list_plugins(self) -> list[BasePlugin]:
        return list(self._plugins.values())
