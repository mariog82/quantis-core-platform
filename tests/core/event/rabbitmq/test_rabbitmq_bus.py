from core.event import (
    Event,
    EventType,
    InMemoryRabbitMQClient,
    RabbitMQEventBus,
)


def test_rabbitmq_event_bus_publishes_and_reads_queue():
    bus = RabbitMQEventBus(
        client=InMemoryRabbitMQClient(),
    )
    bus.subscribe(
        "document.approved",
        lambda envelope: None,
        subscriber_name="document-projection",
    )

    event = Event(
        EventType("document.approved"),
        {"document_id": "doc-1"},
    )
    result = bus.publish(event)
    records = bus.read_queue(
        "document.approved",
        subscriber_name="document-projection",
    )

    assert result.event_id == event.event_id.value
    assert len(records) == 1
    assert records[0].event.payload["document_id"] == "doc-1"


def test_rabbitmq_event_bus_invokes_subscriber():
    bus = RabbitMQEventBus(
        client=InMemoryRabbitMQClient(),
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
