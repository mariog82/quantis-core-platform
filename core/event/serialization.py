from abc import ABC, abstractmethod
from datetime import datetime
import json
from typing import Any

from core.event.contracts import (
    Event,
    EventEnvelope,
    EventId,
    EventMetadata,
    EventPriority,
    EventStatus,
    EventType,
)


class EventSerializer(ABC):
    @abstractmethod
    def serialize(self, envelope: EventEnvelope) -> str:
        raise NotImplementedError


class EventDeserializer(ABC):
    @abstractmethod
    def deserialize(self, data: str) -> EventEnvelope:
        raise NotImplementedError


class JsonEventSerializer(EventSerializer, EventDeserializer):
    def serialize(self, envelope: EventEnvelope) -> str:
        event = envelope.event
        return json.dumps(
            {
                "event_id": event.event_id.value,
                "event_type": event.event_type.name,
                "payload": event.payload,
                "metadata": {
                    "correlation_id": event.metadata.correlation_id,
                    "causation_id": event.metadata.causation_id,
                    "tenant_id": event.metadata.tenant_id,
                    "user_id": event.metadata.user_id,
                    "source": event.metadata.source,
                    "priority": event.metadata.priority.value,
                    "created_at": event.metadata.created_at.isoformat(),
                    "headers": event.metadata.headers,
                },
                "status": envelope.status.value,
                "attempts": envelope.attempts,
            },
            sort_keys=True,
        )

    def deserialize(self, data: str) -> EventEnvelope:
        raw: dict[str, Any] = json.loads(data)
        metadata_raw = raw["metadata"]
        metadata = EventMetadata(
            correlation_id=metadata_raw.get("correlation_id"),
            causation_id=metadata_raw.get("causation_id"),
            tenant_id=metadata_raw.get("tenant_id"),
            user_id=metadata_raw.get("user_id"),
            source=metadata_raw.get("source", "quantis"),
            priority=EventPriority(metadata_raw.get("priority", "normal")),
            created_at=datetime.fromisoformat(metadata_raw["created_at"]),
            headers=dict(metadata_raw.get("headers", {})),
        )
        event = Event(
            event_id=EventId(raw["event_id"]),
            event_type=EventType(raw["event_type"]),
            payload=dict(raw["payload"]),
            metadata=metadata,
        )
        return EventEnvelope(
            event=event,
            status=EventStatus(raw["status"]),
            attempts=int(raw["attempts"]),
        )
