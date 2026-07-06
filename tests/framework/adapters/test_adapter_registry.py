import pytest

from framework.adapters import AdapterAlreadyRegistered, AdapterNotFound, AdapterRegistry
from framework.adapters.testing import EchoAdapter


def test_adapter_registry_registers_adapter():
    registry = AdapterRegistry()
    adapter = EchoAdapter()

    registry.register(adapter)

    assert registry.exists("echo")
    assert registry.get("echo") == adapter


def test_adapter_registry_rejects_duplicate_adapter():
    registry = AdapterRegistry()
    registry.register(EchoAdapter())

    with pytest.raises(AdapterAlreadyRegistered):
        registry.register(EchoAdapter())


def test_adapter_registry_raises_for_missing_adapter():
    registry = AdapterRegistry()

    with pytest.raises(AdapterNotFound):
        registry.get("missing")


def test_adapter_registry_finds_by_type_and_capability():
    registry = AdapterRegistry()
    registry.register(EchoAdapter())

    assert len(registry.find_by_type("test")) == 1
    assert len(registry.find_by_capability("echo")) == 1
