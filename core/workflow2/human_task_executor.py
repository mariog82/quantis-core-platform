from core.workflow2.definition import WorkflowStepDefinition
from core.workflow2.human_task_service import HumanTaskService
from core.workflow2.human_tasks import HumanTask
from core.workflow2.instance import WorkflowInstance
from core.workflow2.runtime import StepResult


class HumanTaskStepExecutor:
    def __init__(self, service: HumanTaskService) -> None:
        self.service = service

    def supports(self, step: WorkflowStepDefinition) -> bool:
        return step.step_type == "human"

    def execute(
        self,
        step: WorkflowStepDefinition,
        instance: WorkflowInstance,
    ) -> StepResult:
        task = self.service.create(
            HumanTask(
                workflow_instance_id=instance.instance_id.value,
                step_id=step.step_id,
                name=step.name,
                candidate_users=tuple(
                    step.metadata.get("candidate_users", ())
                ),
                candidate_groups=tuple(
                    step.metadata.get("candidate_groups", ())
                ),
                payload=dict(instance.context.data),
            )
        )

        return StepResult(
            success=True,
            output={"human_task_id": task.task_id.value},
            wait=True,
        )
