from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Protocol
from uuid import uuid4


class WorkflowEventType(str, Enum):
    INSTANCE_CREATED = "instance_created"
    INSTANCE_STARTED = "instance_started"
    STEP_STARTED = "step_started"
    STEP_COMPLETED = "step_completed"
    STEP_FAILED = "step_failed"
    INSTANCE_WAITING = "instance_waiting"
    INSTANCE_COMPLETED = "instance_completed"
    INSTANCE_FAILED = "instance_failed"
    INSTANCE_CANCELLED = "instance_cancelled"
    HUMAN_TASK_CREATED = "human_task_created"
    TIMER_SCHEDULED = "timer_scheduled"
    TIMER_FIRED = "timer_fired"
    SAGA_COMPENSATING = "saga_compensating"
    SAGA_COMPENSATED = "saga_compensated"


@dataclass(frozen=True)
class WorkflowMonitoringEvent:
    workflow_instance_id: str
    event_type: WorkflowEventType
    workflow_id: str | None = None
    step_id: str | None = None
    event_id: str = field(default_factory=lambda: str(uuid4()))
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    duration_ms: float | None = None
    tenant_id: str | None = None
    correlation_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class WorkflowMonitoringSink(Protocol):
    def record(self, event: WorkflowMonitoringEvent) -> WorkflowMonitoringEvent:
        ...

    def list_for_instance(
        self,
        workflow_instance_id: str,
    ) -> list[WorkflowMonitoringEvent]:
        ...

    def list_all(self) -> list[WorkflowMonitoringEvent]:
        ...


class InMemoryWorkflowMonitoringSink:
    def __init__(self) -> None:
        self._events: list[WorkflowMonitoringEvent] = []

    def record(self, event: WorkflowMonitoringEvent) -> WorkflowMonitoringEvent:
        self._events.append(event)
        return event

    def list_for_instance(
        self,
        workflow_instance_id: str,
    ) -> list[WorkflowMonitoringEvent]:
        return [
            event
            for event in self._events
            if event.workflow_instance_id == workflow_instance_id
        ]

    def list_all(self) -> list[WorkflowMonitoringEvent]:
        return list(self._events)
