from core.workflow2 import (
    HumanTaskService,
    HumanTaskStepExecutor,
    InMemoryHumanTaskRepository,
    WorkflowId,
    WorkflowInstance,
    WorkflowStepDefinition,
    WorkflowVersion,
)


def test_human_task_executor_creates_task_and_waits():
    repository = InMemoryHumanTaskRepository()
    service = HumanTaskService(repository)
    executor = HumanTaskStepExecutor(service)

    step = WorkflowStepDefinition(
        step_id="review",
        name="Review",
        step_type="human",
        metadata={"candidate_users": ["u1"]},
    )
    instance = WorkflowInstance(
        workflow_id=WorkflowId("document.approval"),
        workflow_version=WorkflowVersion(1),
    ).start("review")

    result = executor.execute(step, instance)

    assert result.success is True
    assert result.wait is True
    assert "human_task_id" in result.output
    assert len(repository.list_open()) == 1
