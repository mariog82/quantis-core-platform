from core.workflow2 import (
    InMemoryWorkflowMonitoringSink,
    WorkflowEventType,
    WorkflowMonitoringService,
)


def test_monitoring_summary_calculates_kpis():
    service = WorkflowMonitoringService(
        InMemoryWorkflowMonitoringSink()
    )

    service.record("wf-1", WorkflowEventType.INSTANCE_STARTED)
    service.record(
        "wf-1",
        WorkflowEventType.STEP_COMPLETED,
        duration_ms=100.0,
    )
    service.record(
        "wf-1",
        WorkflowEventType.STEP_COMPLETED,
        duration_ms=300.0,
    )
    service.record("wf-1", WorkflowEventType.INSTANCE_COMPLETED)

    summary = service.summary()

    assert summary.total_events == 4
    assert summary.completed_instances == 1
    assert summary.completed_steps == 2
    assert summary.average_step_duration_ms == 200.0
    assert summary.completion_rate == 1.0
    assert summary.failure_rate == 0.0
