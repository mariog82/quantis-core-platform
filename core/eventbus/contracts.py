from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Callable
from uuid import uuid4

@dataclass(frozen=True)
class EventId:
    value: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class DomainEvent:
    id: EventId
    event_type: str
    aggregate_id: str
    tenant_id: str | None = None
    payload: dict = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

EventHandler = Callable[[DomainEvent], None]

class EventPublisher:
    def publish(self, event: DomainEvent) -> None:
        raise NotImplementedError

class EventSubscriber:
    def subscribe(self, event_type: str, handler: EventHandler) -> None:
        raise NotImplementedError
