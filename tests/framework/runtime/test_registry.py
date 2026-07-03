from framework.contracts.module import BaseModule, ModuleManifest
from framework.runtime import ModuleRegistry, ModuleState
class DemoModule(BaseModule):
    manifest = ModuleManifest(name='demo', version='0.1.0', capabilities=['demo'])
    def boot(self): pass
    def shutdown(self): pass

def test_register_module():
    registry = ModuleRegistry(); module = registry.register(DemoModule())
    assert module.manifest.name == 'demo'; assert registry.exists('demo'); assert registry.state('demo') == ModuleState.REGISTERED

def test_find_by_capability():
    registry = ModuleRegistry(); registry.register(DemoModule())
    assert len(registry.find_by_capability('demo')) == 1
