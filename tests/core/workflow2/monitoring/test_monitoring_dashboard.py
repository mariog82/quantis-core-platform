from core.workflow2 import (
    InMemoryWorkflowMonitoringSink,
    WorkflowEventType,
    WorkflowMonitoringDashboard,
    WorkflowMonitoringService,
)


def test_monitoring_dashboard_returns_snapshot():
    service = WorkflowMonitoringService(
        InMemoryWorkflowMonitoringSink()
    )
    service.record("wf-1", WorkflowEventType.INSTANCE_STARTED)

    dashboard = WorkflowMonitoringDashboard(service)
    snapshot = dashboard.snapshot()

    assert snapshot["summary"]["started_instances"] == 1
    assert snapshot["health"]["active_instances"] == 1
    assert snapshot["active_instances"] == ["wf-1"]
