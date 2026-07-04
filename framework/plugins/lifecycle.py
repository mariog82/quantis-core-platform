from framework.contracts.plugin import BasePlugin


class PluginLifecycleManager:
    def install(self, plugin: BasePlugin) -> BasePlugin:
        plugin.install()
        return plugin

    def enable(self, plugin: BasePlugin) -> BasePlugin:
        plugin.enable()
        return plugin

    def disable(self, plugin: BasePlugin) -> BasePlugin:
        plugin.disable()
        return plugin
