from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


class EventStatus(str, Enum):
    PENDING = "pending"
    RECORDED = "recorded"
    SERIALIZED = "serialized"
    INVALID = "invalid"


class EventPriority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class EventId:
    value: str = field(default_factory=lambda: str(uuid4()))


@dataclass(frozen=True)
class EventType:
    name: str

    def __post_init__(self) -> None:
        if not self.name or "." not in self.name:
            raise ValueError("EventType must use dotted notation, e.g. tenant.created")


@dataclass(frozen=True)
class EventMetadata:
    correlation_id: str | None = None
    causation_id: str | None = None
    tenant_id: str | None = None
    user_id: str | None = None
    source: str = "quantis"
    priority: EventPriority = EventPriority.NORMAL
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    headers: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class Event:
    event_type: EventType
    payload: dict[str, Any]
    event_id: EventId = field(default_factory=EventId)
    metadata: EventMetadata = field(default_factory=EventMetadata)


@dataclass(frozen=True)
class EventEnvelope:
    event: Event
    status: EventStatus = EventStatus.PENDING
    attempts: int = 0

    @property
    def event_id(self) -> str:
        return self.event.event_id.value

    @property
    def type_name(self) -> str:
        return self.event.event_type.name
