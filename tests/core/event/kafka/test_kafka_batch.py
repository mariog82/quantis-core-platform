from core.event import (
    Event,
    EventType,
    InMemoryKafkaClient,
    KafkaEventBus,
)


def test_kafka_event_bus_publishes_batch():
    bus = KafkaEventBus(
        client=InMemoryKafkaClient(),
    )

    results = bus.publish_many(
        [
            Event(EventType("metric.recorded"), {"value": 1}),
            Event(EventType("metric.recorded"), {"value": 2}),
        ]
    )

    records = bus.read_topic("metric.recorded")

    assert len(results) == 2
    assert len(records) == 2
