from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Protocol


@dataclass(frozen=True)
class Snapshot:
    stream_id: str
    version: int
    state: dict[str, Any]
    created_at: datetime


class SnapshotStore(Protocol):
    def save(
        self,
        stream_id: str,
        version: int,
        state: dict[str, Any],
    ) -> Snapshot:
        ...

    def load(self, stream_id: str) -> Snapshot | None:
        ...


class InMemorySnapshotStore:
    def __init__(self) -> None:
        self._snapshots: dict[str, Snapshot] = {}

    def save(
        self,
        stream_id: str,
        version: int,
        state: dict[str, Any],
    ) -> Snapshot:
        snapshot = Snapshot(
            stream_id=stream_id,
            version=version,
            state=dict(state),
            created_at=datetime.now(timezone.utc),
        )
        self._snapshots[stream_id] = snapshot
        return snapshot

    def load(self, stream_id: str) -> Snapshot | None:
        return self._snapshots.get(stream_id)
