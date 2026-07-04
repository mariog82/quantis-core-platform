from framework.contracts.plugin import BasePlugin
from framework.plugins.extension_point import ExtensionPoint, ExtensionPointRegistry
from framework.plugins.lifecycle import PluginLifecycleManager
from framework.plugins.registry import PluginRegistry


class PluginRuntime:
    def __init__(self):
        self.registry = PluginRegistry()
        self.extension_points = ExtensionPointRegistry()
        self.lifecycle = PluginLifecycleManager()

    def register_extension_point(self, name: str, description: str = "") -> ExtensionPoint:
        return self.extension_points.register(ExtensionPoint(name=name, description=description))

    def install(self, plugin: BasePlugin) -> BasePlugin:
        self.registry.register(plugin)
        return self.lifecycle.install(plugin)

    def enable(self, name: str) -> BasePlugin:
        return self.lifecycle.enable(self.registry.get(name))
