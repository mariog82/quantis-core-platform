import pytest

from framework.contracts.plugin import BasePlugin, PluginManifest
from framework.plugins import PluginAlreadyRegistered, PluginRegistry


class DemoPlugin(BasePlugin):
    manifest = PluginManifest(name="demo-plugin", version="0.1.0")


def test_register_plugin():
    registry = PluginRegistry()
    plugin = registry.register(DemoPlugin())

    assert plugin.manifest.name == "demo-plugin"
    assert registry.exists("demo-plugin")


def test_duplicate_plugin_registration_raises():
    registry = PluginRegistry()
    registry.register(DemoPlugin())

    with pytest.raises(PluginAlreadyRegistered):
        registry.register(DemoPlugin())
