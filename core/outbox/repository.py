from dataclasses import replace
from datetime import datetime, timezone
from typing import Protocol

from core.outbox.model import OutboxMessage, OutboxStatus


class OutboxRepository(Protocol):
    def add(self, message: OutboxMessage) -> OutboxMessage:
        ...

    def pending(self, limit: int = 100) -> list[OutboxMessage]:
        ...

    def mark_published(self, message_id: str) -> OutboxMessage:
        ...

    def mark_failed(self, message_id: str, error: str) -> OutboxMessage:
        ...


class InMemoryOutboxRepository:
    def __init__(self) -> None:
        self._messages: dict[str, OutboxMessage] = {}

    def add(self, message: OutboxMessage) -> OutboxMessage:
        self._messages[message.message_id] = message
        return message

    def pending(self, limit: int = 100) -> list[OutboxMessage]:
        return [
            message
            for message in self._messages.values()
            if message.status == OutboxStatus.PENDING
        ][:limit]

    def mark_published(self, message_id: str) -> OutboxMessage:
        message = self._messages[message_id]
        updated = replace(
            message,
            status=OutboxStatus.PUBLISHED,
            attempts=message.attempts + 1,
            published_at=datetime.now(timezone.utc),
            last_error=None,
        )
        self._messages[message_id] = updated
        return updated

    def mark_failed(self, message_id: str, error: str) -> OutboxMessage:
        message = self._messages[message_id]
        updated = replace(
            message,
            status=OutboxStatus.FAILED,
            attempts=message.attempts + 1,
            last_error=error,
        )
        self._messages[message_id] = updated
        return updated
