from core.event import (
    Event,
    EventType,
    InMemoryRabbitMQClient,
    RabbitMQEventBus,
)


def test_rabbitmq_event_bus_publishes_batch():
    bus = RabbitMQEventBus(
        client=InMemoryRabbitMQClient(),
    )
    bus.subscribe(
        "metric.recorded",
        lambda envelope: None,
        subscriber_name="metrics",
    )

    results = bus.publish_many(
        [
            Event(EventType("metric.recorded"), {"value": 1}),
            Event(EventType("metric.recorded"), {"value": 2}),
        ]
    )

    records = bus.read_queue(
        "metric.recorded",
        subscriber_name="metrics",
    )

    assert len(results) == 2
    assert len(records) == 2
