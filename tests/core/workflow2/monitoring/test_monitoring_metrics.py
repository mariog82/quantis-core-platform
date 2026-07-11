from core.workflow2 import WorkflowMonitoringMetrics


def test_monitoring_metrics_defaults():
    metrics = WorkflowMonitoringMetrics()

    assert metrics.events_recorded == 0
    assert metrics.snapshots_generated == 0
    assert metrics.active_instances == 0
    assert metrics.completed_instances == 0
    assert metrics.failed_instances == 0
    assert metrics.monitoring_failures == 0
