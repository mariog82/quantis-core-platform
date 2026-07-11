from core.workflow2 import SagaMetrics


def test_saga_metrics_defaults():
    metrics = SagaMetrics()

    assert metrics.started == 0
    assert metrics.completed == 0
    assert metrics.failed == 0
    assert metrics.compensations_started == 0
    assert metrics.compensations_completed == 0
    assert metrics.compensation_failures == 0
