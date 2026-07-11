from core.event import Event, EventEnvelope, EventType, InMemoryEventDispatcher, InMemoryEventSubscriber


def test_dispatcher_invokes_matching_handlers():
    subscriber = InMemoryEventSubscriber()
    received = []
    subscriber.subscribe(
        "document.approved",
        lambda envelope: received.append(envelope.event.payload["document_id"]),
    )
    dispatcher = InMemoryEventDispatcher(subscriber=subscriber)
    envelope = EventEnvelope(Event(EventType("document.approved"), {"document_id": "doc-1"}))

    result = dispatcher.dispatch(envelope)

    assert received == ["doc-1"]
    assert result.event_id == envelope.event_id
