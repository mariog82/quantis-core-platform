from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Protocol

from core.event import EventEnvelope


@dataclass(frozen=True)
class EventRecord:
    stream_id: str
    version: int
    envelope: EventEnvelope
    recorded_at: datetime


class EventStore(Protocol):
    def append(
        self,
        stream_id: str,
        envelope: EventEnvelope,
        expected_version: int | None = None,
    ) -> EventRecord:
        ...

    def read_stream(
        self,
        stream_id: str,
        from_version: int = 1,
    ) -> list[EventRecord]:
        ...

    def current_version(self, stream_id: str) -> int:
        ...


class InMemoryEventStore:
    def __init__(self) -> None:
        self._streams: dict[str, list[EventRecord]] = {}

    def append(
        self,
        stream_id: str,
        envelope: EventEnvelope,
        expected_version: int | None = None,
    ) -> EventRecord:
        current = self.current_version(stream_id)

        if expected_version is not None and expected_version != current:
            raise ValueError(
                f"Concurrency conflict for {stream_id}: "
                f"expected {expected_version}, current {current}"
            )

        record = EventRecord(
            stream_id=stream_id,
            version=current + 1,
            envelope=envelope,
            recorded_at=datetime.now(timezone.utc),
        )
        self._streams.setdefault(stream_id, []).append(record)
        return record

    def read_stream(
        self,
        stream_id: str,
        from_version: int = 1,
    ) -> list[EventRecord]:
        return [
            record
            for record in self._streams.get(stream_id, [])
            if record.version >= from_version
        ]

    def current_version(self, stream_id: str) -> int:
        return len(self._streams.get(stream_id, []))
