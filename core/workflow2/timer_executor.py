from datetime import datetime, timedelta, timezone

from core.workflow2.definition import WorkflowStepDefinition
from core.workflow2.instance import WorkflowInstance
from core.workflow2.runtime import StepResult
from core.workflow2.scheduler import WorkflowScheduler
from core.workflow2.timers import TimerType, WorkflowTimer


class TimerStepExecutor:
    def __init__(self, scheduler: WorkflowScheduler) -> None:
        self.scheduler = scheduler

    def supports(self, step: WorkflowStepDefinition) -> bool:
        return step.step_type == "timer"

    def execute(
        self,
        step: WorkflowStepDefinition,
        instance: WorkflowInstance,
    ) -> StepResult:
        delay_seconds = float(step.metadata.get("delay_seconds", 0))
        fire_at = datetime.now(timezone.utc) + timedelta(seconds=delay_seconds)

        timer = self.scheduler.schedule(
            WorkflowTimer(
                workflow_instance_id=instance.instance_id.value,
                step_id=step.step_id,
                fire_at=fire_at,
                timer_type=TimerType(
                    step.metadata.get("timer_type", TimerType.DELAY.value)
                ),
                payload=dict(instance.context.data),
            )
        )

        return StepResult(
            success=True,
            output={
                "workflow_timer_id": timer.timer_id.value,
                "workflow_timer_fire_at": timer.fire_at.isoformat(),
            },
            wait=True,
        )
