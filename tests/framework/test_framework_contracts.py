from framework.contracts import BaseController, BasePlugin, BaseService, ModuleManifest, PluginManifest, ServiceContext

class DemoPlugin(BasePlugin):
    manifest = PluginManifest(name="demo-plugin", version="0.1.0")

def test_service_context_defaults():
    service = BaseService(ServiceContext(tenant_id="tenant-demo"))
    assert service.context.tenant_id == "tenant-demo"

def test_controller_ok_and_fail():
    controller = BaseController()
    ok = controller.ok({"value": 1})
    fail = controller.fail("ERR", "Error")
    assert ok.success is True
    assert fail.success is False
    assert fail.error["code"] == "ERR"

def test_plugin_lifecycle():
    plugin = DemoPlugin()
    plugin.enable()
    assert plugin.status == "enabled"
    plugin.disable()
    assert plugin.status == "disabled"

def test_module_manifest():
    manifest = ModuleManifest(name="analytics", version="0.1.0", capabilities=["kpi", "dashboard"])
    assert manifest.name == "analytics"
    assert "kpi" in manifest.capabilities
