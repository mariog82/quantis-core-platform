from core.workflow2 import (
    InMemoryWorkflowTimerRepository,
    TimerStepExecutor,
    WorkflowId,
    WorkflowInstance,
    WorkflowScheduler,
    WorkflowStepDefinition,
    WorkflowVersion,
)


def test_timer_executor_schedules_timer_and_waits():
    repository = InMemoryWorkflowTimerRepository()
    scheduler = WorkflowScheduler(repository)
    executor = TimerStepExecutor(scheduler)

    step = WorkflowStepDefinition(
        step_id="wait-30",
        name="Wait",
        step_type="timer",
        metadata={"delay_seconds": 30},
    )
    instance = WorkflowInstance(
        workflow_id=WorkflowId("delayed.flow"),
        workflow_version=WorkflowVersion(1),
    ).start("wait-30")

    result = executor.execute(step, instance)

    assert result.success is True
    assert result.wait is True
    assert "workflow_timer_id" in result.output
    assert len(scheduler.pending_for_instance(instance.instance_id.value)) == 1
