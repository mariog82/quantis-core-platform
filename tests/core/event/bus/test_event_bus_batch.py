from core.event import Event, EventType, InMemoryEventBus


def test_event_bus_publishes_batch():
    bus = InMemoryEventBus()
    received: list[int] = []
    bus.subscribe("metric.recorded", lambda envelope: received.append(envelope.event.payload["value"]))

    results = bus.publish_many(
        [
            Event(EventType("metric.recorded"), {"value": 1}),
            Event(EventType("metric.recorded"), {"value": 2}),
        ]
    )

    assert len(results) == 2
    assert received == [1, 2]
