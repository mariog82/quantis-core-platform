from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.messaging.contracts import MessageAcknowledgement, MessageEnvelope, MessagePublishRequest, MessageSubscribeRequest


class MessagingAdapter(Adapter):
    metadata = AdapterMetadata(name="messaging", adapter_type="messaging", version="0.5.0-beta.1", capabilities=["messaging"], provider="quantis")

    def publish(self, request: MessagePublishRequest) -> MessageAcknowledgement:
        raise NotImplementedError

    def subscribe(self, request: MessageSubscribeRequest) -> None:
        raise NotImplementedError

    def drain(self, topic: str) -> list[MessageEnvelope]:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}
        if operation == "publish":
            return AdapterResult.ok(self.publish(payload["request"]))
        if operation == "drain":
            return AdapterResult.ok(self.drain(payload["topic"]))
        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryMessagingAdapter(MessagingAdapter):
    def __init__(self):
        super().__init__()
        self._messages: dict[str, list[MessageEnvelope]] = {}
        self._subscribers: dict[str, list] = {}

    def publish(self, request: MessagePublishRequest) -> MessageAcknowledgement:
        envelope = MessageEnvelope(topic=request.topic, message=request.message)
        self._messages.setdefault(request.topic, []).append(envelope)
        for handler in self._subscribers.get(request.topic, []):
            handler(envelope)
        return MessageAcknowledgement(message_id=envelope.message_id)

    def subscribe(self, request: MessageSubscribeRequest) -> None:
        self._subscribers.setdefault(request.topic, []).append(request.handler)

    def drain(self, topic: str) -> list[MessageEnvelope]:
        messages = list(self._messages.get(topic, []))
        self._messages[topic] = []
        return messages
