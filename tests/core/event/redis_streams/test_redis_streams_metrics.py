from core.event import RedisStreamsMetrics


def test_redis_streams_metrics_defaults():
    metrics = RedisStreamsMetrics()

    assert metrics.messages_published == 0
    assert metrics.messages_read == 0
    assert metrics.publish_failures == 0
    assert metrics.read_failures == 0
    assert metrics.active_subscriptions == 0
