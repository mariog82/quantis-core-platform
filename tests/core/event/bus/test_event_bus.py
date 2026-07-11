from core.event import Event, EventType, InMemoryEventBus


def test_event_bus_publishes_and_dispatches():
    bus = InMemoryEventBus()
    received: list[str] = []

    bus.subscribe(
        "tenant.created",
        lambda envelope: received.append(envelope.event.payload["tenant_id"]),
    )

    result = bus.publish(
        Event(
            EventType("tenant.created"),
            {"tenant_id": "tenant-1"},
        )
    )

    assert received == ["tenant-1"]
    assert result.event.payload["tenant_id"] == "tenant-1"
