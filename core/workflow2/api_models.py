from dataclasses import asdict, dataclass, field
from typing import Any

from core.workflow2.definition import WorkflowDefinition
from core.workflow2.instance import WorkflowContext, WorkflowInstance


@dataclass(frozen=True)
class CreateWorkflowInstanceRequest:
    workflow_id: str
    version: int | None = None
    context: dict[str, Any] = field(default_factory=dict)
    tenant_id: str | None = None
    correlation_id: str | None = None
    user_id: str | None = None

    def to_context(self) -> WorkflowContext:
        return WorkflowContext(
            data=dict(self.context),
            tenant_id=self.tenant_id,
            correlation_id=self.correlation_id,
            user_id=self.user_id,
        )


@dataclass(frozen=True)
class CompleteHumanTaskRequest:
    user_id: str
    result: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class WorkflowDefinitionResponse:
    workflow_id: str
    version: int
    name: str
    initial_step_id: str
    steps: list[dict[str, Any]]
    transitions: list[dict[str, Any]]

    @classmethod
    def from_definition(
        cls,
        definition: WorkflowDefinition,
    ) -> "WorkflowDefinitionResponse":
        return cls(
            workflow_id=definition.workflow_id,
            version=definition.version,
            name=definition.name,
            initial_step_id=definition.initial_step_id,
            steps=[asdict(step) for step in definition.steps],
            transitions=[asdict(transition) for transition in definition.transitions],
        )


@dataclass(frozen=True)
class WorkflowInstanceResponse:
    instance_id: str
    workflow_id: str
    workflow_version: int
    state: str
    current_step_id: str | None
    context: dict[str, Any]
    history: list[str]

    @classmethod
    def from_instance(
        cls,
        instance: WorkflowInstance,
    ) -> "WorkflowInstanceResponse":
        return cls(
            instance_id=instance.instance_id.value,
            workflow_id=instance.workflow_id.value,
            workflow_version=instance.workflow_version.value,
            state=instance.state.value,
            current_step_id=instance.current_step_id,
            context=dict(instance.context.data),
            history=list(instance.history),
        )
