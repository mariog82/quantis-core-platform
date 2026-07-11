from core.event import Event, EventEnvelope, EventType
from core.eventstore import InMemoryEventStore


def test_event_store_appends_and_reads_stream():
    store = InMemoryEventStore()
    envelope = EventEnvelope(
        Event(EventType("tenant.created"), {"tenant_id": "t1"})
    )

    record = store.append("tenant-t1", envelope, expected_version=0)

    assert record.version == 1
    assert store.current_version("tenant-t1") == 1
    assert store.read_stream("tenant-t1") == [record]
