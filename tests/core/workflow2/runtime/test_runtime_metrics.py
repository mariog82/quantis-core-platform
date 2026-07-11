from core.workflow2 import WorkflowRuntimeMetrics


def test_runtime_metrics_defaults():
    metrics = WorkflowRuntimeMetrics()

    assert metrics.instances_created == 0
    assert metrics.steps_executed == 0
    assert metrics.steps_failed == 0
    assert metrics.instances_completed == 0
    assert metrics.instances_waiting == 0
