from core.event import SubscriberMetrics


def test_subscriber_metrics_defaults():
    metrics = SubscriberMetrics()

    assert metrics.subscriptions_created == 0
    assert metrics.subscriptions_removed == 0
    assert metrics.handlers_invoked == 0
    assert metrics.handler_failures == 0
