from core.event import KafkaMetrics


def test_kafka_metrics_defaults():
    metrics = KafkaMetrics()

    assert metrics.messages_produced == 0
    assert metrics.messages_consumed == 0
    assert metrics.produce_failures == 0
    assert metrics.consume_failures == 0
    assert metrics.active_subscriptions == 0
