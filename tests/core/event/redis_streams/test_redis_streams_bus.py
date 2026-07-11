from core.event import (
    Event,
    EventType,
    InMemoryRedisStreamsClient,
    RedisStreamsEventBus,
)


def test_redis_streams_event_bus_publishes_and_reads():
    client = InMemoryRedisStreamsClient()
    bus = RedisStreamsEventBus(client=client)

    event = Event(
        EventType("document.approved"),
        {"document_id": "doc-1"},
    )
    result = bus.publish(event)
    records = bus.read_stream("document.approved")

    assert result.event_id == event.event_id.value
    assert len(records) == 1
    assert records[0].event.payload["document_id"] == "doc-1"


def test_redis_streams_event_bus_invokes_subscriber():
    client = InMemoryRedisStreamsClient()
    bus = RedisStreamsEventBus(client=client)
    received: list[str] = []

    bus.subscribe(
        "user.created",
        lambda envelope: received.append(envelope.event.payload["user_id"]),
    )
    bus.publish(Event(EventType("user.created"), {"user_id": "u1"}))

    assert received == ["u1"]
