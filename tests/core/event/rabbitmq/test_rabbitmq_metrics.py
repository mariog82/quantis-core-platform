from core.event import RabbitMQMetrics


def test_rabbitmq_metrics_defaults():
    metrics = RabbitMQMetrics()

    assert metrics.exchanges_declared == 0
    assert metrics.queues_declared == 0
    assert metrics.bindings_created == 0
    assert metrics.messages_published == 0
    assert metrics.messages_consumed == 0
    assert metrics.publish_failures == 0
    assert metrics.consume_failures == 0
