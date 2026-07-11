from dataclasses import dataclass
from typing import Protocol

from core.event.bus import EventBus, EventBusResult
from core.event.contracts import Event, EventEnvelope
from core.event.serialization import JsonEventSerializer
from core.event.subscriber import EventHandler, Subscription, SubscriptionId


class RedisStreamsClient(Protocol):
    def xadd(self, stream: str, fields: dict[str, str]) -> str:
        ...

    def xrange(self, stream: str) -> list[tuple[str, dict[str, str]]]:
        ...


@dataclass(frozen=True)
class RedisStreamsConfig:
    stream_prefix: str = "quantis"
    consumer_group: str = "quantis-core"
    consumer_name: str = "quantis-worker"

    def stream_name(self, topic: str) -> str:
        normalized = topic.replace(".", ":")
        return f"{self.stream_prefix}:{normalized}"


class InMemoryRedisStreamsClient:
    def __init__(self) -> None:
        self._streams: dict[str, list[tuple[str, dict[str, str]]]] = {}
        self._counter = 0

    def xadd(self, stream: str, fields: dict[str, str]) -> str:
        self._counter += 1
        message_id = f"{self._counter}-0"
        self._streams.setdefault(stream, []).append((message_id, dict(fields)))
        return message_id

    def xrange(self, stream: str) -> list[tuple[str, dict[str, str]]]:
        return list(self._streams.get(stream, []))


class RedisStreamsEventBus(EventBus):
    def __init__(
        self,
        client: RedisStreamsClient,
        config: RedisStreamsConfig | None = None,
        serializer: JsonEventSerializer | None = None,
    ) -> None:
        self.client = client
        self.config = config or RedisStreamsConfig()
        self.serializer = serializer or JsonEventSerializer()
        self._subscriptions: dict[str, list[Subscription]] = {}
        self._subscription_counter = 0

    def publish(self, event: Event) -> EventEnvelope:
        return self.publish_with_result(event).dispatched

    def publish_with_result(self, event: Event) -> EventBusResult:
        envelope = EventEnvelope(event)
        stream = self.config.stream_name(event.event_type.name)
        payload = self.serializer.serialize(envelope)
        self.client.xadd(stream, {"payload": payload})

        for subscription in self._subscriptions.get(event.event_type.name, []):
            if subscription.active:
                subscription.handler(envelope)

        return EventBusResult(published=envelope, dispatched=envelope)

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
            subscription_id=SubscriptionId(f"redis-sub-{self._subscription_counter}"),
            topic=topic,
            handler=handler,
            subscriber_name=subscriber_name,
        )
        self._subscriptions.setdefault(topic, []).append(subscription)
        return subscription

    def read_stream(self, topic: str) -> list[EventEnvelope]:
        stream = self.config.stream_name(topic)
        records = self.client.xrange(stream)
        return [
            self.serializer.deserialize(fields["payload"])
            for _, fields in records
        ]
