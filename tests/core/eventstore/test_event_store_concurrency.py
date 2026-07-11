import pytest

from core.event import Event, EventEnvelope, EventType
from core.eventstore import InMemoryEventStore


def test_event_store_detects_concurrency_conflict():
    store = InMemoryEventStore()
    envelope = EventEnvelope(Event(EventType("user.created"), {}))
    store.append("user-u1", envelope, expected_version=0)

    with pytest.raises(ValueError):
        store.append("user-u1", envelope, expected_version=0)
