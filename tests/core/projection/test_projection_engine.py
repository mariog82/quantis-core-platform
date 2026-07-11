from core.event import Event, EventEnvelope, EventType
from core.eventstore import EventRecord
from core.projection import (
    InMemoryProjectionEngine,
    ProjectionDefinition,
)
from datetime import datetime, timezone


class TenantProjectionHandler:
    def key_for(self, record: EventRecord) -> str:
        return record.envelope.event.payload["tenant_id"]

    def apply(self, current_state, record: EventRecord):
        state = dict(current_state)
        state["tenant_id"] = record.envelope.event.payload["tenant_id"]
        state["active"] = True
        return state


def test_projection_engine_builds_read_state():
    engine = InMemoryProjectionEngine()
    engine.register(
        ProjectionDefinition(
            name="tenant-summary",
            event_types=("tenant.created",),
        ),
        TenantProjectionHandler(),
    )

    record = EventRecord(
        stream_id="tenant-t1",
        version=1,
        envelope=EventEnvelope(
            Event(
                EventType("tenant.created"),
                {"tenant_id": "t1"},
            )
        ),
        recorded_at=datetime.now(timezone.utc),
    )

    checkpoints = engine.project(record)

    assert checkpoints[0].event_version == 1
    assert engine.store.get("tenant-summary", "t1") == {
        "tenant_id": "t1",
        "active": True,
    }
