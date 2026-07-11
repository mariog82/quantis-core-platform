from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from typing import Protocol

from core.event.contracts import EventEnvelope, EventStatus


@dataclass(frozen=True)
class DeadLetterId:
    value: str


@dataclass(frozen=True)
class DeadLetterEntry:
    dead_letter_id: DeadLetterId
    envelope: EventEnvelope
    reason: str
    source: str = "dispatcher"
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    replayed_at: datetime | None = None
    replay_count: int = 0

    @property
    def replayed(self) -> bool:
        return self.replayed_at is not None


class DeadLetterQueue(Protocol):
    def add(
        self,
        envelope: EventEnvelope,
        reason: str,
        source: str = "dispatcher",
    ) -> DeadLetterEntry:
        ...

    def get(self, dead_letter_id: DeadLetterId) -> DeadLetterEntry | None:
        ...

    def list_entries(self) -> list[DeadLetterEntry]:
        ...

    def replay(self, dead_letter_id: DeadLetterId) -> EventEnvelope | None:
        ...

    def remove(self, dead_letter_id: DeadLetterId) -> bool:
        ...


class InMemoryDeadLetterQueue:
    def __init__(self) -> None:
        self._entries: dict[str, DeadLetterEntry] = {}
        self._counter = 0

    def add(
        self,
        envelope: EventEnvelope,
        reason: str,
        source: str = "dispatcher",
    ) -> DeadLetterEntry:
        self._counter += 1
        failed = replace(
            envelope,
            status=EventStatus.INVALID,
            attempts=envelope.attempts + 1,
        )
        entry = DeadLetterEntry(
            dead_letter_id=DeadLetterId(f"dlq-{self._counter}"),
            envelope=failed,
            reason=reason,
            source=source,
        )
        self._entries[entry.dead_letter_id.value] = entry
        return entry

    def get(self, dead_letter_id: DeadLetterId) -> DeadLetterEntry | None:
        return self._entries.get(dead_letter_id.value)

    def list_entries(self) -> list[DeadLetterEntry]:
        return list(self._entries.values())

    def replay(self, dead_letter_id: DeadLetterId) -> EventEnvelope | None:
        entry = self.get(dead_letter_id)
        if entry is None:
            return None

        self._entries[dead_letter_id.value] = replace(
            entry,
            replayed_at=datetime.now(timezone.utc),
            replay_count=entry.replay_count + 1,
        )
        return replace(entry.envelope, status=EventStatus.PENDING)

    def remove(self, dead_letter_id: DeadLetterId) -> bool:
        return self._entries.pop(dead_letter_id.value, None) is not None
