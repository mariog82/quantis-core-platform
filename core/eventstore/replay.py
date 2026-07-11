from typing import Callable, Any

from core.eventstore.store import EventRecord, EventStore
from core.eventstore.snapshot import SnapshotStore


class EventReplayService:
    def __init__(
        self,
        event_store: EventStore,
        snapshot_store: SnapshotStore | None = None,
    ) -> None:
        self.event_store = event_store
        self.snapshot_store = snapshot_store

    def replay(
        self,
        stream_id: str,
        reducer: Callable[[dict[str, Any], EventRecord], dict[str, Any]],
        initial_state: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        state = dict(initial_state or {})
        from_version = 1

        if self.snapshot_store is not None:
            snapshot = self.snapshot_store.load(stream_id)
            if snapshot is not None:
                state = dict(snapshot.state)
                from_version = snapshot.version + 1

        for record in self.event_store.read_stream(stream_id, from_version):
            state = reducer(state, record)

        return state
