import pytest

from core.event import DispatcherFactory, InMemoryEventDispatcher


def test_dispatcher_factory_creates_memory_dispatcher():
    assert isinstance(DispatcherFactory.create(), InMemoryEventDispatcher)


def test_dispatcher_factory_rejects_unknown_backend():
    with pytest.raises(ValueError):
        DispatcherFactory.create("unknown")
