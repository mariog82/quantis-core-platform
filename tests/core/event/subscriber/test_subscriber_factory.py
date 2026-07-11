import pytest

from core.event import InMemoryEventSubscriber, SubscriberFactory


def test_subscriber_factory_creates_memory_subscriber():
    assert isinstance(SubscriberFactory.create(), InMemoryEventSubscriber)


def test_subscriber_factory_rejects_unknown_backend():
    with pytest.raises(ValueError):
        SubscriberFactory.create("unknown")
