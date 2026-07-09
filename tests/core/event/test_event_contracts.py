from core.event import Event, EventPriority, EventType

def test_event_contract_defaults():
    event = Event(event_type=EventType("tenant.created"), payload={"tenant_id": "demo"})

    assert event.event_id.value
    assert event.metadata.source == "quantis"
    assert event.metadata.priority == EventPriority.NORMAL
