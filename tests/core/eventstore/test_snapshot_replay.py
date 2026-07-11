from core.event import Event, EventEnvelope, EventType
from core.eventstore import (
    EventReplayService,
    InMemoryEventStore,
    InMemorySnapshotStore,
)


def test_replay_uses_snapshot_and_remaining_events():
    store = InMemoryEventStore()
    snapshots = InMemorySnapshotStore()

    store.append(
        "counter-1",
        EventEnvelope(Event(EventType("counter.incremented"), {"value": 1})),
    )
    snapshots.save("counter-1", 1, {"count": 1})
    store.append(
        "counter-1",
        EventEnvelope(Event(EventType("counter.incremented"), {"value": 2})),
    )

    replay = EventReplayService(store, snapshots)

    state = replay.replay(
        "counter-1",
        lambda current, record: {
            "count": current["count"] + record.envelope.event.payload["value"]
        },
    )

    assert state == {"count": 3}
