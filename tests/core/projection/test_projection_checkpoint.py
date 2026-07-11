from datetime import datetime, timezone

from core.event import Event, EventEnvelope, EventType
from core.eventstore import EventRecord
from core.projection import InMemoryProjectionEngine, ProjectionDefinition


class Handler:
    def key_for(self, record):
        return "global"

    def apply(self, current_state, record):
        return {"count": current_state.get("count", 0) + 1}


def test_projection_checkpoint_is_recorded():
    engine = InMemoryProjectionEngine()
    engine.register(
        ProjectionDefinition(
            "event-count",
            ("metric.recorded",),
        ),
        Handler(),
    )
    record = EventRecord(
        "metrics",
        3,
        EventEnvelope(Event(EventType("metric.recorded"), {})),
        datetime.now(timezone.utc),
    )

    engine.project(record)

    checkpoint = engine.checkpoint("event-count", "metrics")
    assert checkpoint is not None
    assert checkpoint.event_version == 3
