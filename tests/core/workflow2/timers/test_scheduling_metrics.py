from core.workflow2 import WorkflowSchedulingMetrics


def test_scheduling_metrics_defaults():
    metrics = WorkflowSchedulingMetrics()

    assert metrics.scheduled == 0
    assert metrics.fired == 0
    assert metrics.cancelled == 0
    assert metrics.expired == 0
    assert metrics.scheduler_failures == 0
