from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable
from uuid import uuid4


class WorkflowExecutionStatus(str, Enum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


@dataclass(frozen=True)
class WorkflowId:
    value: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class WorkflowContext:
    tenant_id: str | None = None
    actor_id: str | None = None
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkflowStep:
    name: str
    handler: Callable[[WorkflowContext], WorkflowContext]
    description: str = ""

    def execute(self, context: WorkflowContext) -> WorkflowContext:
        return self.handler(context)


@dataclass
class Workflow:
    id: WorkflowId
    name: str
    version: str = "0.1.0"
    description: str = ""
    steps: list[WorkflowStep] = field(default_factory=list)

    def add_step(self, step: WorkflowStep) -> None:
        self.steps.append(step)


@dataclass
class WorkflowExecution:
    workflow_id: WorkflowId
    status: WorkflowExecutionStatus = WorkflowExecutionStatus.CREATED
    context: WorkflowContext = field(default_factory=WorkflowContext)
    executed_steps: list[str] = field(default_factory=list)
    error: str | None = None
