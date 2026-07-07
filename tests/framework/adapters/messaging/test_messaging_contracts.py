from framework.adapters.messaging import Message, MessagePriority, MessagePublishRequest

def test_message_publish_request_defaults():
    message = Message(payload={"event": "created"})
    request = MessagePublishRequest(topic="events", message=message)
    assert request.topic == "events"
    assert request.message.priority == MessagePriority.NORMAL
