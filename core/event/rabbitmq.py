from dataclasses import dataclass
from typing import Protocol

from core.event.bus import EventBus, EventBusResult
from core.event.contracts import Event, EventEnvelope
from core.event.serialization import JsonEventSerializer
from core.event.subscriber import EventHandler, Subscription, SubscriptionId


class RabbitMQClient(Protocol):
    def declare_exchange(self, exchange: str, exchange_type: str = "topic") -> None:
        ...

    def declare_queue(self, queue: str) -> None:
        ...

    def bind_queue(self, queue: str, exchange: str, routing_key: str) -> None:
        ...

    def publish(self, exchange: str, routing_key: str, body: str) -> str:
        ...

    def get_messages(self, queue: str) -> list[tuple[str, str]]:
        ...


@dataclass(frozen=True)
class RabbitMQConfig:
    exchange: str = "quantis.events"
    exchange_type: str = "topic"
    queue_prefix: str = "quantis"
    durable: bool = True

    def queue_name(self, topic: str, subscriber_name: str = "default") -> str:
        normalized_topic = topic.replace(".", "-")
        normalized_subscriber = subscriber_name.replace(".", "-")
        return f"{self.queue_prefix}-{normalized_subscriber}-{normalized_topic}"


class InMemoryRabbitMQClient:
    def __init__(self) -> None:
        self.exchanges: dict[str, str] = {}
        self.queues: dict[str, list[tuple[str, str]]] = {}
        self.bindings: list[tuple[str, str, str]] = []
        self._counter = 0

    def declare_exchange(self, exchange: str, exchange_type: str = "topic") -> None:
        self.exchanges[exchange] = exchange_type

    def declare_queue(self, queue: str) -> None:
        self.queues.setdefault(queue, [])

    def bind_queue(self, queue: str, exchange: str, routing_key: str) -> None:
        binding = (queue, exchange, routing_key)
        if binding not in self.bindings:
            self.bindings.append(binding)

    def publish(self, exchange: str, routing_key: str, body: str) -> str:
        self._counter += 1
        message_id = f"rabbit-{self._counter}"

        for queue, bound_exchange, bound_routing_key in self.bindings:
            if bound_exchange == exchange and bound_routing_key == routing_key:
                self.queues.setdefault(queue, []).append((message_id, body))

        return message_id

    def get_messages(self, queue: str) -> list[tuple[str, str]]:
        return list(self.queues.get(queue, []))


class RabbitMQEventBus(EventBus):
    def __init__(
        self,
        client: RabbitMQClient,
        config: RabbitMQConfig | None = None,
        serializer: JsonEventSerializer | None = None,
    ) -> None:
        self.client = client
        self.config = config or RabbitMQConfig()
        self.serializer = serializer or JsonEventSerializer()
        self._subscriptions: dict[str, list[Subscription]] = {}
        self._subscription_counter = 0
        self.client.declare_exchange(
            self.config.exchange,
            self.config.exchange_type,
        )

    def publish(self, event: Event) -> EventEnvelope:
        return self.publish_with_result(event).dispatched

    def publish_with_result(self, event: Event) -> EventBusResult:
        envelope = EventEnvelope(event)
        payload = self.serializer.serialize(envelope)
        routing_key = event.event_type.name

        self.client.publish(
            exchange=self.config.exchange,
            routing_key=routing_key,
            body=payload,
        )

        for subscription in self._subscriptions.get(routing_key, []):
            if subscription.active:
                subscription.handler(envelope)

        return EventBusResult(
            published=envelope,
            dispatched=envelope,
        )

    def publish_many(self, events: list[Event]) -> list[EventEnvelope]:
        return [self.publish(event) for event in events]

    def subscribe(
        self,
        topic: str,
        handler: EventHandler,
        subscriber_name: str = "default",
    ) -> Subscription:
        self._subscription_counter += 1
        queue = self.config.queue_name(topic, subscriber_name)

        self.client.declare_queue(queue)
        self.client.bind_queue(
            queue=queue,
            exchange=self.config.exchange,
            routing_key=topic,
        )

        subscription = Subscription(
            subscription_id=SubscriptionId(
                f"rabbit-sub-{self._subscription_counter}"
            ),
            topic=topic,
            handler=handler,
            subscriber_name=subscriber_name,
        )
        self._subscriptions.setdefault(topic, []).append(subscription)
        return subscription

    def read_queue(
        self,
        topic: str,
        subscriber_name: str = "default",
    ) -> list[EventEnvelope]:
        queue = self.config.queue_name(topic, subscriber_name)
        messages = self.client.get_messages(queue)
        return [
            self.serializer.deserialize(body)
            for _, body in messages
        ]
