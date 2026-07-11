from core.event import Event, EventEnvelope, EventMetadata, EventPriority, EventStatus, EventType, JsonEventSerializer


def test_json_event_serializer_roundtrip():
    serializer = JsonEventSerializer()
    event = Event(
        event_type=EventType("document.approved"),
        payload={"document_id": "doc-1"},
        metadata=EventMetadata(tenant_id="tenant-1", priority=EventPriority.HIGH),
    )
    envelope = EventEnvelope(event=event, status=EventStatus.RECORDED, attempts=1)

    restored = serializer.deserialize(serializer.serialize(envelope))

    assert restored.event_id == envelope.event_id
    assert restored.type_name == "document.approved"
    assert restored.event.payload["document_id"] == "doc-1"
    assert restored.event.metadata.tenant_id == "tenant-1"
    assert restored.event.metadata.priority == EventPriority.HIGH
    assert restored.status == EventStatus.RECORDED
    assert restored.attempts == 1
