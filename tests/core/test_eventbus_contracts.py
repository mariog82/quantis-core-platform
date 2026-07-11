from core.eventbus import EventBusService

def test_emit_event_records_event():
    service = EventBusService()
    event = service.emit("tenant.created", "tenant-1", tenant_id="tenant-1", payload={"name": "Demo"})
    assert event.event_type == "tenant.created"
    assert service.bus.published[0].aggregate_id == "tenant-1"

def test_subscriber_receives_event():
    service = EventBusService()
    received = []
    service.on("identity.created", received.append)
    service.emit("identity.created", "identity-1")
    assert len(received) == 1
    assert received[0].aggregate_id == "identity-1"

def test_wildcard_subscriber_receives_all_events():
    service = EventBusService()
    received = []
    service.on("*", received.append)
    service.emit("a", "1")
    service.emit("b", "2")
    assert len(received) == 2
