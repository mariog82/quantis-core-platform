from core.event import InMemoryEventSubscriber


def test_unsubscribe_removes_subscription():
    subscriber = InMemoryEventSubscriber()
    subscription = subscriber.subscribe("user.created", lambda envelope: None)

    removed = subscriber.unsubscribe(subscription.subscription_id)

    assert removed is True
    assert subscriber.subscriptions_for("user.created") == []
