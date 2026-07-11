from dataclasses import replace
from typing import Protocol

from core.event.contracts import EventEnvelope, EventStatus
from core.event.deadletter import DeadLetterQueue, InMemoryDeadLetterQueue
from core.event.retry import RetryPolicy
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
        dead_letter_queue: DeadLetterQueue | None = None,
        retry_policy: RetryPolicy | None = None,
    ) -> None:
        self.subscriber = subscriber or InMemoryEventSubscriber()
        self.router = router or EventRouter()
        self.dead_letter_queue = dead_letter_queue or InMemoryDeadLetterQueue()
        self.retry_policy = retry_policy or RetryPolicy()
        self._middleware: list[EventMiddleware] = []
        self._interceptors: list[EventInterceptor] = []

    def use(self, middleware: EventMiddleware) -> None:
        self._middleware.append(middleware)

    def add_interceptor(self, interceptor: EventInterceptor) -> None:
        self._interceptors.append(interceptor)

    def dispatch(self, envelope: EventEnvelope) -> EventEnvelope:
        current = envelope

        try:
            for middleware in self._middleware:
                current = middleware(current)

            for interceptor in self._interceptors:
                interceptor.before_dispatch(current)

            topic = self.router.topic_for(current)
            for subscription in self.subscriber.subscriptions_for(topic):
                if subscription.active:
                    subscription.handler(current)

            dispatched = replace(current, status=EventStatus.RECORDED)

            for interceptor in self._interceptors:
                interceptor.after_dispatch(dispatched)

            return dispatched
        except Exception as exc:
            failed = replace(
                current,
                status=EventStatus.INVALID,
                attempts=current.attempts + 1,
            )

            if not self.retry_policy.should_retry(failed.attempts):
                self.dead_letter_queue.add(
                    failed,
                    reason=str(exc),
                    source="dispatcher",
                )

            return failed
