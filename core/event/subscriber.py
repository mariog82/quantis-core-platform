from dataclasses import dataclass, field
from typing import Protocol

from core.event.contracts import EventEnvelope


class EventHandler(Protocol):
    def __call__(self, envelope: EventEnvelope) -> None:
        ...


@dataclass(frozen=True)
class SubscriptionId:
    value: str


@dataclass(frozen=True)
class Subscription:
    subscription_id: SubscriptionId
    topic: str
    handler: EventHandler
    subscriber_name: str
    active: bool = True
    metadata: dict[str, str] = field(default_factory=dict)


class EventSubscriber:
    def subscribe(
        self,
        topic: str,
        handler: EventHandler,
        subscriber_name: str = "default",
        metadata: dict[str, str] | None = None,
    ) -> Subscription:
        raise NotImplementedError

    def unsubscribe(self, subscription_id: SubscriptionId) -> bool:
        raise NotImplementedError

    def subscriptions_for(self, topic: str) -> list[Subscription]:
        raise NotImplementedError


class InMemoryEventSubscriber(EventSubscriber):
    def __init__(self) -> None:
        self._subscriptions: dict[str, list[Subscription]] = {}
        self._counter = 0

    def subscribe(
        self,
        topic: str,
        handler: EventHandler,
        subscriber_name: str = "default",
        metadata: dict[str, str] | None = None,
    ) -> Subscription:
        self._counter += 1
        subscription = Subscription(
            subscription_id=SubscriptionId(f"sub-{self._counter}"),
            topic=topic,
            handler=handler,
            subscriber_name=subscriber_name,
            metadata=dict(metadata or {}),
        )
        self._subscriptions.setdefault(topic, []).append(subscription)
        return subscription

    def unsubscribe(self, subscription_id: SubscriptionId) -> bool:
        for topic, subscriptions in self._subscriptions.items():
            remaining = [
                subscription
                for subscription in subscriptions
                if subscription.subscription_id != subscription_id
            ]
            if len(remaining) != len(subscriptions):
                self._subscriptions[topic] = remaining
                return True
        return False

    def subscriptions_for(self, topic: str) -> list[Subscription]:
        return list(self._subscriptions.get(topic, []))
