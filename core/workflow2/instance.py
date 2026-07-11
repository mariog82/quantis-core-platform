from dataclasses import dataclass, field, replace
from enum import Enum
from typing import Any
from uuid import uuid4


@dataclass(frozen=True)
class WorkflowId:
    value: str


@dataclass(frozen=True)
class WorkflowVersion:
    value: int


@dataclass(frozen=True)
class WorkflowInstanceId:
    value: str = field(default_factory=lambda: str(uuid4()))


class WorkflowState(str, Enum):
    CREATED = "created"
    RUNNING = "running"
    WAITING = "waiting"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass(frozen=True)
class WorkflowContext:
    data: dict[str, Any] = field(default_factory=dict)
    tenant_id: str | None = None
    correlation_id: str | None = None
    user_id: str | None = None


@dataclass(frozen=True)
class WorkflowInstance:
    workflow_id: WorkflowId
    workflow_version: WorkflowVersion
    instance_id: WorkflowInstanceId = field(default_factory=WorkflowInstanceId)
    state: WorkflowState = WorkflowState.CREATED
    current_step_id: str | None = None
    context: WorkflowContext = field(default_factory=WorkflowContext)
    history: tuple[str, ...] = ()

    def start(self, initial_step_id: str) -> "WorkflowInstance":
        return replace(
            self,
            state=WorkflowState.RUNNING,
            current_step_id=initial_step_id,
            history=self.history + (initial_step_id,),
        )

    def move_to(self, step_id: str) -> "WorkflowInstance":
        return replace(
            self,
            current_step_id=step_id,
            history=self.history + (step_id,),
        )

    def complete(self) -> "WorkflowInstance":
        return replace(self, state=WorkflowState.COMPLETED)

    def fail(self) -> "WorkflowInstance":
        return replace(self, state=WorkflowState.FAILED)
