from framework.contracts import ModuleManifest
from framework.runtime.registry import ModuleRegistry


class DemoModule:
    manifest = ModuleManifest(name="demo", version="0.1.0")


def test_register_module():
    registry = ModuleRegistry()
    module = DemoModule()

    registry.register(module)

    assert registry.exists("demo") is True
    assert registry.get("demo") == module


def test_unregister_module():
    registry = ModuleRegistry()
    module = DemoModule()

    registry.register(module)
    registry.unregister("demo")

    assert registry.exists("demo") is False


def test_list_modules():
    registry = ModuleRegistry()
    registry.register(DemoModule())

    assert len(registry.list()) == 1