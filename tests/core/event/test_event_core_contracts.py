import pytest

from core.event import Event, EventEnvelope, EventMetadata, EventPriority, EventStatus, EventType


def test_event_core_contract_defaults():
    event = Event(event_type=EventType("tenant.created"), payload={"tenant_id": "demo"})
    envelope = EventEnvelope(event=event)

    assert event.event_id.value
    assert event.metadata.source == "quantis"
    assert event.metadata.priority == EventPriority.NORMAL
    assert envelope.status == EventStatus.PENDING
    assert envelope.type_name == "tenant.created"


def test_event_type_requires_dotted_notation():
    with pytest.raises(ValueError):
        EventType("invalid")


def test_event_metadata_supports_tenant_and_correlation():
    metadata = EventMetadata(tenant_id="tenant-1", correlation_id="corr-1", headers={"x": "y"})

    assert metadata.tenant_id == "tenant-1"
    assert metadata.correlation_id == "corr-1"
    assert metadata.headers["x"] == "y"
