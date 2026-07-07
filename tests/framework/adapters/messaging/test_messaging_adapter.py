from framework.adapters.messaging import InMemoryMessagingAdapter, Message, MessagePublishRequest, MessageSubscribeRequest

def test_in_memory_messaging_adapter_publishes_and_drains():
    adapter = InMemoryMessagingAdapter()
    ack = adapter.publish(MessagePublishRequest(topic="events", message=Message(payload={"id": 1})))
    drained = adapter.drain("events")
    assert ack.accepted is True
    assert len(drained) == 1
    assert drained[0].message.payload == {"id": 1}
    assert adapter.drain("events") == []

def test_in_memory_messaging_adapter_calls_subscriber():
    adapter = InMemoryMessagingAdapter()
    received = []
    adapter.subscribe(MessageSubscribeRequest(topic="events", handler=lambda envelope: received.append(envelope)))
    adapter.publish(MessagePublishRequest(topic="events", message=Message(payload={"id": 2})))
    assert len(received) == 1
    assert received[0].message.payload == {"id": 2}

def test_messaging_adapter_execute_publish_and_drain():
    adapter = InMemoryMessagingAdapter()
    publish_result = adapter.execute("publish", {"request": MessagePublishRequest(topic="events", message=Message(payload={"ok": True}))})
    drain_result = adapter.execute("drain", {"topic": "events"})
    assert publish_result.success is True
    assert drain_result.success is True
    assert drain_result.data[0].message.payload == {"ok": True}
