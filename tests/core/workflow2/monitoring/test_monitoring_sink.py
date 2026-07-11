from core.workflow2 import (
    InMemoryWorkflowMonitoringSink,
    WorkflowEventType,
    WorkflowMonitoringEvent,
)


def test_monitoring_sink_records_and_filters_events():
    sink = InMemoryWorkflowMonitoringSink()

    first = sink.record(
        WorkflowMonitoringEvent(
            workflow_instance_id="wf-1",
            workflow_id="tenant.provisioning",
            event_type=WorkflowEventType.INSTANCE_STARTED,
        )
    )
    sink.record(
        WorkflowMonitoringEvent(
            workflow_instance_id="wf-2",
            workflow_id="document.approval",
            event_type=WorkflowEventType.INSTANCE_STARTED,
        )
    )

    assert sink.list_for_instance("wf-1") == [first]
    assert len(sink.list_all()) == 2
