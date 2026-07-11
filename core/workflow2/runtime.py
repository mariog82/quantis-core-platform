from dataclasses import dataclass, replace
from typing import Any, Protocol

from core.workflow2.definition import (
    WorkflowDefinition,
    WorkflowStepDefinition,
)
from core.workflow2.exceptions import (
    InvalidWorkflowDefinition,
    WorkflowDefinitionNotFound,
)
from core.workflow2.instance import (
    WorkflowContext,
    WorkflowId,
    WorkflowInstance,
    WorkflowState,
    WorkflowVersion,
)
from core.workflow2.registry import WorkflowRegistry
from core.workflow2.validation import WorkflowDefinitionValidator


@dataclass(frozen=True)
class StepResult:
    success: bool
    output: dict[str, Any]
    next_step_id: str | None = None
    wait: bool = False
    error: str | None = None


class StepExecutor(Protocol):
    def supports(self, step: WorkflowStepDefinition) -> bool:
        ...

    def execute(
        self,
        step: WorkflowStepDefinition,
        instance: WorkflowInstance,
    ) -> StepResult:
        ...


class WorkflowRuntime:
    def __init__(
        self,
        registry: WorkflowRegistry,
        validator: WorkflowDefinitionValidator | None = None,
    ) -> None:
        self.registry = registry
        self.validator = validator or WorkflowDefinitionValidator()
        self._executors: list[StepExecutor] = []

    def register_executor(self, executor: StepExecutor) -> None:
        self._executors.append(executor)

    def create_instance(
        self,
        workflow_id: str,
        version: int | None = None,
        context: WorkflowContext | None = None,
    ) -> WorkflowInstance:
        definition = self._resolve_definition(workflow_id, version)
        report = self.validator.validate(definition)
        if not report.passed:
            raise InvalidWorkflowDefinition(
                ", ".join(issue.code for issue in report.issues)
            )

        return WorkflowInstance(
            workflow_id=WorkflowId(definition.workflow_id),
            workflow_version=WorkflowVersion(definition.version),
            context=context or WorkflowContext(),
        ).start(definition.initial_step_id)

    def execute_current_step(
        self,
        instance: WorkflowInstance,
    ) -> WorkflowInstance:
        if instance.state != WorkflowState.RUNNING:
            return instance

        definition = self.registry.get(
            instance.workflow_id.value,
            instance.workflow_version.value,
        )

        if instance.current_step_id is None:
            return instance.fail()

        step = definition.step(instance.current_step_id)
        if step is None:
            return instance.fail()

        executor = next(
            (
                current
                for current in self._executors
                if current.supports(step)
            ),
            None,
        )
        if executor is None:
            return instance.fail()

        result = executor.execute(step, instance)

        if not result.success:
            return replace(
                instance,
                state=WorkflowState.FAILED,
                context=self._merge_context(
                    instance.context,
                    result.output,
                ),
            )

        updated = replace(
            instance,
            context=self._merge_context(
                instance.context,
                result.output,
            ),
        )

        if result.wait:
            return replace(updated, state=WorkflowState.WAITING)

        next_step_id = result.next_step_id or self._default_next_step(
            definition,
            step.step_id,
        )

        if next_step_id is None:
            return updated.complete()

        return updated.move_to(next_step_id)

    def run_until_wait_or_complete(
        self,
        instance: WorkflowInstance,
        max_steps: int = 100,
    ) -> WorkflowInstance:
        current = instance

        for _ in range(max_steps):
            if current.state in {
                WorkflowState.WAITING,
                WorkflowState.COMPLETED,
                WorkflowState.FAILED,
                WorkflowState.CANCELLED,
            }:
                return current

            previous_step = current.current_step_id
            current = self.execute_current_step(current)

            if (
                current.state == WorkflowState.RUNNING
                and current.current_step_id == previous_step
            ):
                return current.fail()

        return current.fail()

    def _resolve_definition(
        self,
        workflow_id: str,
        version: int | None,
    ) -> WorkflowDefinition:
        try:
            if version is None:
                return self.registry.latest(workflow_id)
            return self.registry.get(workflow_id, version)
        except WorkflowDefinitionNotFound:
            raise

    @staticmethod
    def _default_next_step(
        definition: WorkflowDefinition,
        step_id: str,
    ) -> str | None:
        transitions = definition.outgoing(step_id)
        if not transitions:
            return None
        return transitions[0].target_step_id

    @staticmethod
    def _merge_context(
        context: WorkflowContext,
        output: dict[str, Any],
    ) -> WorkflowContext:
        data = dict(context.data)
        data.update(output)
        return WorkflowContext(
            data=data,
            tenant_id=context.tenant_id,
            correlation_id=context.correlation_id,
            user_id=context.user_id,
        )
