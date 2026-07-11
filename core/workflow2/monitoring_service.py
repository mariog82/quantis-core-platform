from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone

from core.workflow2.monitoring import (
    WorkflowEventType,
    WorkflowMonitoringEvent,
    WorkflowMonitoringSink,
)


@dataclass(frozen=True)
class WorkflowMonitoringSummary:
    total_events: int
    started_instances: int
    completed_instances: int
    failed_instances: int
    waiting_instances: int
    completed_steps: int
    failed_steps: int
    average_step_duration_ms: float
    completion_rate: float
    failure_rate: float


class WorkflowMonitoringService:
    def __init__(self, sink: WorkflowMonitoringSink) -> None:
        self.sink = sink

    def record(
        self,
        workflow_instance_id: str,
        event_type: WorkflowEventType,
        *,
        workflow_id: str | None = None,
        step_id: str | None = None,
        duration_ms: float | None = None,
        tenant_id: str | None = None,
        correlation_id: str | None = None,
        metadata: dict | None = None,
    ) -> WorkflowMonitoringEvent:
        return self.sink.record(
            WorkflowMonitoringEvent(
                workflow_instance_id=workflow_instance_id,
                workflow_id=workflow_id,
                step_id=step_id,
                event_type=event_type,
                duration_ms=duration_ms,
                tenant_id=tenant_id,
                correlation_id=correlation_id,
                metadata=dict(metadata or {}),
            )
        )

    def summary(self) -> WorkflowMonitoringSummary:
        events = self.sink.list_all()
        counts = Counter(event.event_type for event in events)

        durations = [
            event.duration_ms
            for event in events
            if event.duration_ms is not None
            and event.event_type == WorkflowEventType.STEP_COMPLETED
        ]

        started = counts[WorkflowEventType.INSTANCE_STARTED]
        completed = counts[WorkflowEventType.INSTANCE_COMPLETED]
        failed = counts[WorkflowEventType.INSTANCE_FAILED]
        denominator = started if started > 0 else 1

        return WorkflowMonitoringSummary(
            total_events=len(events),
            started_instances=started,
            completed_instances=completed,
            failed_instances=failed,
            waiting_instances=counts[WorkflowEventType.INSTANCE_WAITING],
            completed_steps=counts[WorkflowEventType.STEP_COMPLETED],
            failed_steps=counts[WorkflowEventType.STEP_FAILED],
            average_step_duration_ms=(
                sum(durations) / len(durations) if durations else 0.0
            ),
            completion_rate=completed / denominator,
            failure_rate=failed / denominator,
        )

    def history(
        self,
        workflow_instance_id: str,
    ) -> list[WorkflowMonitoringEvent]:
        return sorted(
            self.sink.list_for_instance(workflow_instance_id),
            key=lambda event: event.occurred_at,
        )

    def active_instances(self) -> set[str]:
        active: set[str] = set()
        terminal = {
            WorkflowEventType.INSTANCE_COMPLETED,
            WorkflowEventType.INSTANCE_FAILED,
            WorkflowEventType.INSTANCE_CANCELLED,
        }

        for event in self.sink.list_all():
            if event.event_type == WorkflowEventType.INSTANCE_STARTED:
                active.add(event.workflow_instance_id)
            elif event.event_type in terminal:
                active.discard(event.workflow_instance_id)

        return active

    def health(self) -> dict[str, object]:
        summary = self.summary()
        return {
            "status": "degraded" if summary.failure_rate > 0.25 else "healthy",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "active_instances": len(self.active_instances()),
            "completion_rate": summary.completion_rate,
            "failure_rate": summary.failure_rate,
        }
