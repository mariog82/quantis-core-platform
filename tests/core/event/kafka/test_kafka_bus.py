from core.event import (
    Event,
    EventType,
    InMemoryKafkaClient,
    KafkaEventBus,
)


def test_kafka_event_bus_publishes_and_reads_topic():
    bus = KafkaEventBus(
        client=InMemoryKafkaClient(),
    )

    event = Event(
        EventType("document.approved"),
        {"document_id": "doc-1"},
    )
    result = bus.publish(event)
    records = bus.read_topic("document.approved")

    assert result.event_id == event.event_id.value
    assert len(records) == 1
    assert records[0].event.payload["document_id"] == "doc-1"


def test_kafka_event_bus_invokes_subscriber():
    bus = KafkaEventBus(
        client=InMemoryKafkaClient(),
    )
    received: list[str] = []

    bus.subscribe(
        "user.created",
        lambda envelope: received.append(
            envelope.event.payload["user_id"]
        ),
    )
    bus.publish(
        Event(
            EventType("user.created"),
            {"user_id": "u1"},
        )
    )

    assert received == ["u1"]
