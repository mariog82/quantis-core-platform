from collections.abc import Callable
from dataclasses import dataclass

from core.workflow2.definition import WorkflowStepDefinition
from core.workflow2.instance import WorkflowInstance
from core.workflow2.runtime import StepResult


@dataclass
class FunctionStepExecutor:
    step_type: str
    handler: Callable[
        [WorkflowStepDefinition, WorkflowInstance],
        StepResult,
    ]

    def supports(self, step: WorkflowStepDefinition) -> bool:
        return step.step_type == self.step_type

    def execute(
        self,
        step: WorkflowStepDefinition,
        instance: WorkflowInstance,
    ) -> StepResult:
        return self.handler(step, instance)


class NoOpStepExecutor:
    def __init__(self, step_type: str = "service") -> None:
        self.step_type = step_type

    def supports(self, step: WorkflowStepDefinition) -> bool:
        return step.step_type == self.step_type

    def execute(
        self,
        step: WorkflowStepDefinition,
        instance: WorkflowInstance,
    ) -> StepResult:
        return StepResult(
            success=True,
            output={"last_step": step.step_id},
        )
