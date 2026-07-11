from core.workflow2 import (
    FunctionStepExecutor,
    InMemoryWorkflowRegistry,
    StepResult,
    WorkflowDefinition,
    WorkflowRuntime,
    WorkflowState,
    WorkflowStepDefinition,
)


def test_runtime_marks_failed_step():
    registry = InMemoryWorkflowRegistry()
    registry.register(
        WorkflowDefinition(
            workflow_id="broken.flow",
            version=1,
            name="Broken",
            initial_step_id="fail",
            steps=(
                WorkflowStepDefinition(
                    step_id="fail",
                    name="Fail",
                    step_type="custom",
                ),
            ),
        )
    )
    runtime = WorkflowRuntime(registry)
    runtime.register_executor(
        FunctionStepExecutor(
            "custom",
            lambda step, instance: StepResult(
                success=False,
                output={"reason": "boom"},
                error="boom",
            ),
        )
    )

    failed = runtime.execute_current_step(
        runtime.create_instance("broken.flow")
    )

    assert failed.state == WorkflowState.FAILED
    assert failed.context.data["reason"] == "boom"
