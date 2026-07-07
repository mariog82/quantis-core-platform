from abc import abstractmethod
from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.messaging.contracts import (
    MessageAcknowledgement,
    MessageEnvelope,
    MessagePublishRequest,
    MessageSubscribeRequest,
    MessagingProviderType,
)

class MessagingAdapter(Adapter):
    metadata = AdapterMetadata(
        name="messaging",
        adapter_type="messaging",
        version="0.5.0-alpha.6",
        description="Provider-neutral messaging adapter contract.",
        capabilities=["messaging", "events", "queue", "pubsub"],
        provider="quantis",
    )

    @abstractmethod
    def publish(self, request: MessagePublishRequest) -> MessageAcknowledgement:
        raise NotImplementedError

    @abstractmethod
    def subscribe(self, request: MessageSubscribeRequest) -> None:
        raise NotImplementedError

    @abstractmethod
    def drain(self, topic: str) -> list[MessageEnvelope]:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}
        if operation == "publish":
            request = payload.get("request")
            if not isinstance(request, MessagePublishRequest):
                return AdapterResult.fail("INVALID_MESSAGE_PUBLISH_REQUEST")
            return AdapterResult.ok(self.publish(request))
        if operation == "subscribe":
            request = payload.get("request")
            if not isinstance(request, MessageSubscribeRequest):
                return AdapterResult.fail("INVALID_MESSAGE_SUBSCRIBE_REQUEST")
            self.subscribe(request)
            return AdapterResult.ok({"subscribed": request.topic})
        if operation == "drain":
            topic = payload.get("topic")
            if not isinstance(topic, str):
                return AdapterResult.fail("INVALID_MESSAGE_TOPIC")
            return AdapterResult.ok(self.drain(topic))
        return AdapterResult.fail("UNSUPPORTED_OPERATION")

class InMemoryMessagingAdapter(MessagingAdapter):
    metadata = AdapterMetadata(
        name="memory-messaging",
        adapter_type="messaging",
        version="0.5.0-alpha.6",
        description="In-memory messaging adapter for tests.",
        capabilities=["messaging", "events", "queue", "pubsub"],
        provider=MessagingProviderType.MEMORY.value,
    )

    def __init__(self):
        super().__init__()
        self._messages: dict[str, list[MessageEnvelope]] = {}
        self._subscribers: dict[str, list] = {}

    def publish(self, request: MessagePublishRequest) -> MessageAcknowledgement:
        envelope = MessageEnvelope(topic=request.topic, message=request.message)
        self._messages.setdefault(request.topic, []).append(envelope)
        for handler in self._subscribers.get(request.topic, []):
            handler(envelope)
        return MessageAcknowledgement(message_id=envelope.message_id, accepted=True)

    def subscribe(self, request: MessageSubscribeRequest) -> None:
        self._subscribers.setdefault(request.topic, []).append(request.handler)

    def drain(self, topic: str) -> list[MessageEnvelope]:
        messages = list(self._messages.get(topic, []))
        self._messages[topic] = []
        return messages
