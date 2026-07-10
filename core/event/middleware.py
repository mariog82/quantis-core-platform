from dataclasses import replace
from typing import Callable

from core.event.contracts import EventEnvelope, EventMetadata


class CorrelationMiddleware:
    def __init__(self, correlation_id_factory: Callable[[], str]) -> None:
        self._correlation_id_factory = correlation_id_factory

    def __call__(self, envelope: EventEnvelope) -> EventEnvelope:
        metadata = envelope.event.metadata
        if metadata.correlation_id:
            return envelope

        updated_metadata = EventMetadata(
            correlation_id=self._correlation_id_factory(),
            causation_id=metadata.causation_id,
            tenant_id=metadata.tenant_id,
            user_id=metadata.user_id,
            source=metadata.source,
            priority=metadata.priority,
            created_at=metadata.created_at,
            headers=dict(metadata.headers),
        )
        updated_event = replace(envelope.event, metadata=updated_metadata)
        return replace(envelope, event=updated_event)


class HeaderMiddleware:
    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value

    def __call__(self, envelope: EventEnvelope) -> EventEnvelope:
        metadata = envelope.event.metadata
        headers = dict(metadata.headers)
        headers[self.key] = self.value

        updated_metadata = EventMetadata(
            correlation_id=metadata.correlation_id,
            causation_id=metadata.causation_id,
            tenant_id=metadata.tenant_id,
            user_id=metadata.user_id,
            source=metadata.source,
            priority=metadata.priority,
            created_at=metadata.created_at,
            headers=headers,
        )
        updated_event = replace(envelope.event, metadata=updated_metadata)
        return replace(envelope, event=updated_event)
