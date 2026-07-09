from core.event import Event, EventEnvelope, EventType, JsonEventSerializer


def test_json_event_serializer_roundtrip():
    serializer = JsonEventSerializer()
    envelope = EventEnvelope(Event(EventType("user.created"), {"user_id": "u1"}))

    restored = serializer.deserialize(serializer.serialize(envelope))

    assert restored.event.event_type.name == "user.created"
    assert restored.event.payload["user_id"] == "u1"
