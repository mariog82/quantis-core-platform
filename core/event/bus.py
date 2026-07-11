from dataclasses import dataclass

from core.event.contracts import Event, EventEnvelope
from core.event.deadletter import DeadLetterQueue, InMemoryDeadLetterQueue
from core.event.dispatcher import InMemoryEventDispatcher
from core.event.publisher import InMemoryPublisher
from core.event.retry import RetryPolicy
from core.event.subscriber import EventHandler, InMemoryEventSubscriber, Subscription


@dataclass(frozen=True)
class EventBusResult:
    published: EventEnvelope
    dispatched: EventEnvelope


class EventBus:
    def publish(self, event: Event) -> EventEnvelope:
        raise NotImplementedError

    def publish_with_result(self, event: Event) -> EventBusResult:
        raise NotImplementedError

    def publish_many(self, events: list[Event]) -> list[EventEnvelope]:
        raise NotImplementedError

    def subscribe(
        self,
        topic: str,
        handler: EventHandler,
        subscriber_name: str = "default",
    ) -> Subscription:
        raise NotImplementedError


class InMemoryEventBus(EventBus):
    def __init__(
        self,
        publisher: InMemoryPublisher | None = None,
        subscriber: InMemoryEventSubscriber | None = None,
        dispatcher: InMemoryEventDispatcher | None = None,
        dead_letter_queue: DeadLetterQueue | None = None,
        retry_policy: RetryPolicy | None = None,
    ) -> None:
        self.publisher = publisher or InMemoryPublisher()
        self.subscriber = subscriber or InMemoryEventSubscriber()
        self.dead_letter_queue = dead_letter_queue or InMemoryDeadLetterQueue()
        self.retry_policy = retry_policy or RetryPolicy()
        self.dispatcher = dispatcher or InMemoryEventDispatcher(
            subscriber=self.subscriber,
            dead_letter_queue=self.dead_letter_queue,
            retry_policy=self.retry_policy,
        )

    def publish(self, event: Event) -> EventEnvelope:
        return self.publish_with_result(event).dispatched

    def publish_with_result(self, event: Event) -> EventBusResult:
        published = self.publisher.publish(event)
        dispatched = self.dispatcher.dispatch(published)
        return EventBusResult(published=published, dispatched=dispatched)

    def publish_many(self, events: list[Event]) -> list[EventEnvelope]:
        return [self.publish(event) for event in events]

    def subscribe(
        self,
        topic: str,
        handler: EventHandler,
        subscriber_name: str = "default",
    ) -> Subscription:
        return self.subscriber.subscribe(topic, handler, subscriber_name)
