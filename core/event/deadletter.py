from dataclasses import dataclass, field
from datetime import datetime, timezone

from core.event.contracts import EventEnvelope


@dataclass(frozen=True)
class DeadLetterEntry:
    envelope: EventEnvelope
    reason: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class DeadLetterQueue:
    def add(self, envelope: EventEnvelope, reason: str) -> DeadLetterEntry:
        raise NotImplementedError

    def list_entries(self) -> list[DeadLetterEntry]:
        raise NotImplementedError


class InMemoryDeadLetterQueue(DeadLetterQueue):
    def __init__(self) -> None:
        self.entries: list[DeadLetterEntry] = []

    def add(self, envelope: EventEnvelope, reason: str) -> DeadLetterEntry:
        entry = DeadLetterEntry(envelope=envelope, reason=reason)
        self.entries.append(entry)
        return entry

    def list_entries(self) -> list[DeadLetterEntry]:
        return list(self.entries)
