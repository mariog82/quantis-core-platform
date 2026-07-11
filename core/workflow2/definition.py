from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class WorkflowStepDefinition:
    step_id: str
    name: str
    step_type: str = "service"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class WorkflowTransition:
    source_step_id: str
    target_step_id: str
    condition: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class WorkflowDefinition:
    workflow_id: str
    version: int
    name: str
    initial_step_id: str
    steps: tuple[WorkflowStepDefinition, ...]
    transitions: tuple[WorkflowTransition, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)

    def step(self, step_id: str) -> WorkflowStepDefinition | None:
        return next((step for step in self.steps if step.step_id == step_id), None)

    def outgoing(self, step_id: str) -> tuple[WorkflowTransition, ...]:
        return tuple(
            transition
            for transition in self.transitions
            if transition.source_step_id == step_id
        )
