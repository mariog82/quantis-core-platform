from core.workflow2 import (
    FunctionStepExecutor,
    InMemoryWorkflowRegistry,
    StepResult,
    WorkflowDefinition,
    WorkflowRuntime,
    WorkflowState,
    WorkflowStepDefinition,
)


def test_runtime_enters_waiting_state():
    registry = InMemoryWorkflowRegistry()
    registry.register(
        WorkflowDefinition(
            workflow_id="human.review",
            version=1,
            name="Human Review",
            initial_step_id="review",
            steps=(
                WorkflowStepDefinition(
                    step_id="review",
                    name="Review",
                    step_type="human",
                ),
            ),
        )
    )
    runtime = WorkflowRuntime(registry)
    runtime.register_executor(
        FunctionStepExecutor(
            "human",
            lambda step, instance: StepResult(
                success=True,
                output={"task": step.step_id},
                wait=True,
            ),
        )
    )

    waiting = runtime.execute_current_step(
        runtime.create_instance("human.review")
    )

    assert waiting.state == WorkflowState.WAITING
    assert waiting.context.data["task"] == "review"
