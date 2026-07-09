from core.event import Event, EventType, InMemoryEventBus


def test_in_memory_event_bus_dispatches_to_subscriber():
    received = []
    bus = InMemoryEventBus()
    bus.subscribe("document.approved", lambda envelope: received.append(envelope.event.payload["document_id"]))

    envelope = bus.publish(Event(EventType("document.approved"), {"document_id": "d1"}))

    assert envelope.status.value == "dispatched"
    assert received == ["d1"]
