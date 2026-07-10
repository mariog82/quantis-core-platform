from dataclasses import replace
from typing import Protocol

from core.event.contracts import EventEnvelope, EventStatus
from core.event.subscriber import EventSubscriber, InMemoryEventSubscriber


class EventMiddleware(Protocol):
    def __call__(self, envelope: EventEnvelope) -> EventEnvelope:
        ...


class EventInterceptor(Protocol):
    def before_dispatch(self, envelope: EventEnvelope) -> None:
        ...

    def after_dispatch(self, envelope: EventEnvelope) -> None:
        ...


class EventRouter:
    def topic_for(self, envelope: EventEnvelope) -> str:
        return envelope.type_name


class EventDispatcher:
    def dispatch(self, envelope: EventEnvelope) -> EventEnvelope:
        raise NotImplementedError


class InMemoryEventDispatcher(EventDispatcher):
    def __init__(
        self,
        subscriber: EventSubscriber | None = None,
        router: EventRouter | None = None,
    ) -> None:
        self.subscriber = subscriber or InMemoryEventSubscriber()
        self.router = router or EventRouter()
        self._middleware: list[EventMiddleware] = []
        self._interceptors: list[EventInterceptor] = []

    def use(self, middleware: EventMiddleware) -> None:
        self._middleware.append(middleware)

    def add_interceptor(self, interceptor: EventInterceptor) -> None:
        self._interceptors.append(interceptor)

    def dispatch(self, envelope: EventEnvelope) -> EventEnvelope:
        current = envelope

        for middleware in self._middleware:
            current = middleware(current)

        for interceptor in self._interceptors:
            interceptor.before_dispatch(current)

        topic = self.router.topic_for(current)
        subscriptions = self.subscriber.subscriptions_for(topic)

        for subscription in subscriptions:
            if subscription.active:
                subscription.handler(current)

        dispatched = replace(current, status=EventStatus.RECORDED)

        for interceptor in self._interceptors:
            interceptor.after_dispatch(dispatched)

        return dispatched
