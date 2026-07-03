from framework.contracts.plugin import BasePlugin, PluginManifest
from framework.plugins import PluginRuntime


class DemoPlugin(BasePlugin):
    manifest = PluginManifest(
        name="demo-plugin",
        version="0.1.0",
        extension_points=["dashboard.widget"],
    )


def test_plugin_runtime_install_enable_and_extension_point():
    runtime = PluginRuntime()
    runtime.register_extension_point("dashboard.widget")

    plugin = runtime.install(DemoPlugin())
    runtime.enable(plugin.manifest.name)

    assert runtime.registry.get("demo-plugin").status == "enabled"
    assert len(runtime.list_extension_points()) == 1


def test_plugin_runtime_attach_handler():
    runtime = PluginRuntime()
    runtime.register_extension_point("report.export")

    handler = object()
    runtime.attach("report.export", handler)

    assert runtime.extension_points.get("report.export").handlers == [handler]
