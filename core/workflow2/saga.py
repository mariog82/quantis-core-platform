from dataclasses import dataclass, field, replace
from enum import Enum
from typing import Any, Protocol
from uuid import uuid4


class SagaStatus(str, Enum):
    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    COMPENSATING = "compensating"
    COMPENSATED = "compensated"


@dataclass(frozen=True)
class SagaId:
    value: str = field(default_factory=lambda: str(uuid4()))


@dataclass(frozen=True)
class SagaStep:
    step_id: str
    action: str
    compensation: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class SagaDefinition:
    saga_type: str
    version: int
    steps: tuple[SagaStep, ...]


@dataclass(frozen=True)
class SagaInstance:
    definition: SagaDefinition
    saga_id: SagaId = field(default_factory=SagaId)
    status: SagaStatus = SagaStatus.CREATED
    current_index: int = 0
    completed_steps: tuple[str, ...] = ()
    compensated_steps: tuple[str, ...] = ()
    context: dict[str, Any] = field(default_factory=dict)
    error: str | None = None

    @property
    def current_step(self) -> SagaStep | None:
        if self.current_index >= len(self.definition.steps):
            return None
        return self.definition.steps[self.current_index]


@dataclass(frozen=True)
class SagaActionResult:
    success: bool
    output: dict[str, Any] = field(default_factory=dict)
    error: str | None = None


class SagaActionExecutor(Protocol):
    def execute(
        self,
        action: str,
        context: dict[str, Any],
    ) -> SagaActionResult:
        ...

    def compensate(
        self,
        compensation: str,
        context: dict[str, Any],
    ) -> SagaActionResult:
        ...


class SagaEngine:
    def __init__(self, executor: SagaActionExecutor) -> None:
        self.executor = executor

    def start(
        self,
        definition: SagaDefinition,
        context: dict[str, Any] | None = None,
    ) -> SagaInstance:
        return SagaInstance(
            definition=definition,
            status=SagaStatus.RUNNING,
            context=dict(context or {}),
        )

    def run(self, instance: SagaInstance) -> SagaInstance:
        current = instance

        while current.status == SagaStatus.RUNNING:
            step = current.current_step
            if step is None:
                return replace(current, status=SagaStatus.COMPLETED)

            result = self.executor.execute(step.action, dict(current.context))
            merged_context = dict(current.context)
            merged_context.update(result.output)

            if not result.success:
                failed = replace(
                    current,
                    status=SagaStatus.FAILED,
                    context=merged_context,
                    error=result.error or f"Action failed: {step.action}",
                )
                return self.compensate(failed)

            current = replace(
                current,
                current_index=current.current_index + 1,
                completed_steps=current.completed_steps + (step.step_id,),
                context=merged_context,
            )

        return current

    def compensate(self, instance: SagaInstance) -> SagaInstance:
        current = replace(instance, status=SagaStatus.COMPENSATING)

        completed = list(current.completed_steps)
        for step_id in reversed(completed):
            step = next(
                item
                for item in current.definition.steps
                if item.step_id == step_id
            )

            if step.compensation is None:
                continue

            result = self.executor.compensate(
                step.compensation,
                dict(current.context),
            )

            merged_context = dict(current.context)
            merged_context.update(result.output)

            if not result.success:
                return replace(
                    current,
                    status=SagaStatus.FAILED,
                    context=merged_context,
                    error=result.error or (
                        f"Compensation failed: {step.compensation}"
                    ),
                )

            current = replace(
                current,
                compensated_steps=current.compensated_steps + (step.step_id,),
                context=merged_context,
            )

        return replace(current, status=SagaStatus.COMPENSATED)
