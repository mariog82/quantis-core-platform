from abc import ABC, abstractmethod
from typing import Protocol

from core.event.contracts import EventEnvelope, EventStatus
from core.event.subscriber import InMemoryEventSubscriber


class EventMiddleware(Protocol):
    def __call__(self, envelope: EventEnvelope) -> EventEnvelope:
        ...


class EventRouter:
    def topic_for(self, envelope: EventEnvelope) -> str:
        return envelope.event.event_type.name


class EventDispatcher(ABC):
    @abstractmethod
    def dispatch(self, envelope: EventEnvelope) -> EventEnvelope:
        raise NotImplementedError


class InMemoryEventDispatcher(EventDispatcher):
    def __init__(self, subscriber: InMemoryEventSubscriber | None = None, router: EventRouter | None = None) -> None:
        self.subscriber = subscriber or InMemoryEventSubscriber()
        self.router = router or EventRouter()
        self.middleware: list[EventMiddleware] = []

    def use(self, middleware: EventMiddleware) -> None:
        self.middleware.append(middleware)

    def dispatch(self, envelope: EventEnvelope) -> EventEnvelope:
        current = envelope
        for middleware in self.middleware:
            current = middleware(current)

        topic = self.router.topic_for(current)
        for subscription in self.subscriber.subscriptions_for(topic):
            subscription.handler(current)

        return EventEnvelope(event=current.event, status=EventStatus.DISPATCHED, attempts=current.attempts)
