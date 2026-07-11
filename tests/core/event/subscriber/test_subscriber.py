from core.event import Event, EventEnvelope, EventType, InMemoryEventSubscriber


def test_subscriber_registers_and_returns_subscription():
    subscriber = InMemoryEventSubscriber()
    subscription = subscriber.subscribe(
        "tenant.created",
        lambda envelope: None,
        subscriber_name="tenant-projection",
    )

    assert subscription.topic == "tenant.created"
    assert subscription.subscriber_name == "tenant-projection"
    assert subscriber.subscriptions_for("tenant.created") == [subscription]


def test_subscriber_handler_can_be_invoked():
    subscriber = InMemoryEventSubscriber()
    received = []
    subscription = subscriber.subscribe(
        "tenant.created",
        lambda envelope: received.append(envelope.event.payload["tenant_id"]),
    )
    envelope = EventEnvelope(Event(EventType("tenant.created"), {"tenant_id": "t1"}))

    subscription.handler(envelope)

    assert received == ["t1"]
