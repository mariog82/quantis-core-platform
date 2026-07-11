from core.event import Event, EventEnvelope, EventRouter, EventType


def test_router_uses_event_type_name():
    router = EventRouter()
    envelope = EventEnvelope(Event(EventType("tenant.created"), {}))

    assert router.topic_for(envelope) == "tenant.created"
