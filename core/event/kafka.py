from dataclasses import dataclass
from typing import Protocol

from core.event.bus import EventBus, EventBusResult
from core.event.contracts import Event, EventEnvelope
from core.event.serialization import JsonEventSerializer
from core.event.subscriber import EventHandler, Subscription, SubscriptionId


class KafkaClient(Protocol):
    def produce(
        self,
        topic: str,
        key: str,
        value: str,
        headers: dict[str, str] | None = None,
    ) -> str:
        ...

    def consume(self, topic: str) -> list[tuple[str, str, dict[str, str]]]:
        ...


@dataclass(frozen=True)
class KafkaConfig:
    topic_prefix: str = "quantis"
    consumer_group: str = "quantis-core"
    client_id: str = "quantis-core-platform"
    auto_offset_reset: str = "earliest"

    def topic_name(self, event_type: str) -> str:
        normalized = event_type.replace(".", "-")
        return f"{self.topic_prefix}-{normalized}"


class InMemoryKafkaClient:
    def __init__(self) -> None:
        self._topics: dict[str, list[tuple[str, str, dict[str, str]]]] = {}
        self._counter = 0

    def produce(
        self,
        topic: str,
        key: str,
        value: str,
        headers: dict[str, str] | None = None,
    ) -> str:
        self._counter += 1
        offset = str(self._counter - 1)
        record = (key, value, dict(headers or {}))
        self._topics.setdefault(topic, []).append(record)
        return offset

    def consume(self, topic: str) -> list[tuple[str, str, dict[str, str]]]:
        return list(self._topics.get(topic, []))


class KafkaEventBus(EventBus):
    def __init__(
        self,
        client: KafkaClient,
        config: KafkaConfig | None = None,
        serializer: JsonEventSerializer | None = None,
    ) -> None:
        self.client = client
        self.config = config or KafkaConfig()
        self.serializer = serializer or JsonEventSerializer()
        self._subscriptions: dict[str, list[Subscription]] = {}
        self._subscription_counter = 0

    def publish(self, event: Event) -> EventEnvelope:
        return self.publish_with_result(event).dispatched

    def publish_with_result(self, event: Event) -> EventBusResult:
        envelope = EventEnvelope(event)
        topic = self.config.topic_name(event.event_type.name)
        value = self.serializer.serialize(envelope)
        headers = {
            "event_type": event.event_type.name,
            "source": event.metadata.source,
        }

        self.client.produce(
            topic=topic,
            key=event.event_id.value,
            value=value,
            headers=headers,
        )

        for subscription in self._subscriptions.get(event.event_type.name, []):
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
        subscription = Subscription(
            subscription_id=SubscriptionId(
                f"kafka-sub-{self._subscription_counter}"
            ),
            topic=topic,
            handler=handler,
            subscriber_name=subscriber_name,
        )
        self._subscriptions.setdefault(topic, []).append(subscription)
        return subscription

    def read_topic(self, event_type: str) -> list[EventEnvelope]:
        topic = self.config.topic_name(event_type)
        records = self.client.consume(topic)
        return [
            self.serializer.deserialize(value)
            for _, value, _ in records
        ]
