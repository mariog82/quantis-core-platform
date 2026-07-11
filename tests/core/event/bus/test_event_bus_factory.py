import pytest

from core.event import EventBusFactory, InMemoryEventBus


def test_event_bus_factory_creates_memory_bus():
    assert isinstance(EventBusFactory.create(), InMemoryEventBus)


def test_event_bus_factory_rejects_unknown_backend():
    with pytest.raises(ValueError):
        EventBusFactory.create("unknown")
