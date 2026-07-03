from framework.contracts.plugin import BasePlugin, PluginManifest
from framework.plugins import PluginLifecycleManager


class DemoPlugin(BasePlugin):
    manifest = PluginManifest(name="demo-plugin", version="0.1.0")


def test_plugin_lifecycle_enable_disable():
    plugin = DemoPlugin()
    lifecycle = PluginLifecycleManager()

    lifecycle.install(plugin)
    assert plugin.status == "installed"

    lifecycle.enable(plugin)
    assert plugin.status == "enabled"

    lifecycle.disable(plugin)
    assert plugin.status == "disabled"
