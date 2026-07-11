from core.event import EventBusMetrics


def test_event_bus_metrics_defaults():
    metrics = EventBusMetrics()

    assert metrics.published == 0
    assert metrics.dispatched == 0
    assert metrics.failed == 0
    assert metrics.subscribers == 0
    assert metrics.batches == 0
