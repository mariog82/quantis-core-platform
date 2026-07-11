from core.workflow2 import (
    InMemoryWorkflowMonitoringSink,
    WorkflowEventType,
    WorkflowMonitoringService,
)


def test_monitoring_health_detects_degraded_failure_rate():
    service = WorkflowMonitoringService(
        InMemoryWorkflowMonitoringSink()
    )

    service.record("wf-1", WorkflowEventType.INSTANCE_STARTED)
    service.record("wf-1", WorkflowEventType.INSTANCE_FAILED)

    health = service.health()

    assert health["status"] == "degraded"
    assert health["failure_rate"] == 1.0
    assert health["active_instances"] == 0
