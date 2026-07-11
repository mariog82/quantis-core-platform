from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4

from core.event import EventEnvelope


class OutboxStatus(str, Enum):
    PENDING = "pending"
    PUBLISHED = "published"
    FAILED = "failed"


@dataclass(frozen=True)
class OutboxMessage:
    envelope: EventEnvelope
    message_id: str = field(default_factory=lambda: str(uuid4()))
    status: OutboxStatus = OutboxStatus.PENDING
    attempts: int = 0
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    published_at: datetime | None = None
    last_error: str | None = None
