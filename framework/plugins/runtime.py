from framework.contracts.plugin import BasePlugin
from framework.plugins.extension_point import ExtensionPoint, ExtensionPointRegistry
from framework.plugins.lifecycle import PluginLifecycleManager
from framework.plugins.registry import PluginRegistry


class PluginRuntime:
    def __init__(
        self,
        registry: PluginRegistry | None = None,
        extension_points: ExtensionPointRegistry | None = None,
        lifecycle: PluginLifecycleManager | None = None,
    ):
        self.registry = registry or PluginRegistry()
        self.extension_points = extension_points or ExtensionPointRegistry()
        self.lifecycle = lifecycle or PluginLifecycleManager()

    def register_extension_point(self, name: str, description: str = "") -> ExtensionPoint:
        return self.extension_points.register(ExtensionPoint(name=name, description=description))

    def install(self, plugin: BasePlugin) -> BasePlugin:
        self.registry.register(plugin)
        return self.lifecycle.install(plugin)

    def enable(self, name: str) -> BasePlugin:
        plugin = self.registry.get(name)
        return self.lifecycle.enable(plugin)

    def disable(self, name: str) -> BasePlugin:
        plugin = self.registry.get(name)
        return self.lifecycle.disable(plugin)

    def attach(self, extension_point: str, handler) -> None:
        self.extension_points.attach(extension_point, handler)

    def list_plugins(self) -> list[BasePlugin]:
        return self.registry.list()

    def list_extension_points(self) -> list[ExtensionPoint]:
        return self.extension_points.list()
