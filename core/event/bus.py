from core.event.contracts import Event, EventEnvelope
from core.event.dispatcher import InMemoryEventDispatcher
from core.event.publisher import InMemoryEventPublisher
from core.event.subscriber import EventHandler, InMemoryEventSubscriber, Subscription


class EventBus:
    def publish(self, event: Event) -> EventEnvelope:
        raise NotImplementedError

    def subscribe(self, topic: str, handler: EventHandler, subscriber_name: str = "default") -> Subscription:
        raise NotImplementedError


class InMemoryEventBus(EventBus):
    def __init__(self) -> None:
        self.subscriber = InMemoryEventSubscriber()
        self.publisher = InMemoryEventPublisher()
        self.dispatcher = InMemoryEventDispatcher(subscriber=self.subscriber)

    def publish(self, event: Event) -> EventEnvelope:
        envelope = self.publisher.publish(event)
        return self.dispatcher.dispatch(envelope)

    def subscribe(self, topic: str, handler: EventHandler, subscriber_name: str = "default") -> Subscription:
        return self.subscriber.subscribe(topic, handler, subscriber_name)
