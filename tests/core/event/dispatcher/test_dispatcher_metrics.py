from core.event import DispatcherMetrics


def test_dispatcher_metrics_defaults():
    metrics = DispatcherMetrics()

    assert metrics.dispatched == 0
    assert metrics.handlers_invoked == 0
    assert metrics.middleware_executed == 0
    assert metrics.interceptor_executed == 0
    assert metrics.failures == 0
