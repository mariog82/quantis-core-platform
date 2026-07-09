from abc import ABC, abstractmethod
from dataclasses import replace

from core.event.contracts import Event, EventEnvelope, EventStatus


class EventPublisher(ABC):
    @abstractmethod
    def publish(self, event: Event) -> EventEnvelope:
        raise NotImplementedError

    @abstractmethod
    def publish_many(self, events: list[Event]) -> list[EventEnvelope]:
        raise NotImplementedError


class InMemoryEventPublisher(EventPublisher):
    def __init__(self) -> None:
        self.published: list[EventEnvelope] = []

    def publish(self, event: Event) -> EventEnvelope:
        envelope = EventEnvelope(event=event, status=EventStatus.PUBLISHED)
        self.published.append(envelope)
        return envelope

    def publish_many(self, events: list[Event]) -> list[EventEnvelope]:
        return [self.publish(event) for event in events]

    def mark_dispatched(self, envelope: EventEnvelope) -> EventEnvelope:
        updated = replace(envelope, status=EventStatus.DISPATCHED)
        return updated
