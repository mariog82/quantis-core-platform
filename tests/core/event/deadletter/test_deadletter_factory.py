import pytest

from core.event import DeadLetterQueueFactory, InMemoryDeadLetterQueue


def test_deadletter_factory_creates_memory_queue():
    assert isinstance(DeadLetterQueueFactory.create(), InMemoryDeadLetterQueue)


def test_deadletter_factory_rejects_unknown_backend():
    with pytest.raises(ValueError):
        DeadLetterQueueFactory.create("unknown")
