from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol

from core.event.contracts import EventEnvelope


class EventHandler(Protocol):
    def __call__(self, envelope: EventEnvelope) -> None:
        ...


@dataclass(frozen=True)
class Subscription:
    topic: str
    handler: EventHandler
    subscriber_name: str = "default"


class EventSubscriber(ABC):
    @abstractmethod
    def subscribe(self, topic: str, handler: EventHandler, subscriber_name: str = "default") -> Subscription:
        raise NotImplementedError

    @abstractmethod
    def subscriptions_for(self, topic: str) -> list[Subscription]:
        raise NotImplementedError


class InMemoryEventSubscriber(EventSubscriber):
    def __init__(self) -> None:
        self._subscriptions: dict[str, list[Subscription]] = {}

    def subscribe(self, topic: str, handler: EventHandler, subscriber_name: str = "default") -> Subscription:
        subscription = Subscription(topic=topic, handler=handler, subscriber_name=subscriber_name)
        self._subscriptions.setdefault(topic, []).append(subscription)
        return subscription

    def subscriptions_for(self, topic: str) -> list[Subscription]:
        return list(self._subscriptions.get(topic, []))
