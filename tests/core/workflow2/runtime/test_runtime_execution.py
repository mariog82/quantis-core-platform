from core.workflow2 import (
    InMemoryWorkflowRegistry,
    NoOpStepExecutor,
    WorkflowDefinition,
    WorkflowRuntime,
    WorkflowState,
    WorkflowStepDefinition,
    WorkflowTransition,
)


def test_runtime_executes_until_completion():
    registry = InMemoryWorkflowRegistry()
    registry.register(
        WorkflowDefinition(
            workflow_id="document.approval",
            version=1,
            name="Document Approval",
            initial_step_id="draft",
            steps=(
                WorkflowStepDefinition("draft", "Draft"),
                WorkflowStepDefinition("approve", "Approve"),
            ),
            transitions=(
                WorkflowTransition("draft", "approve"),
            ),
        )
    )
    runtime = WorkflowRuntime(registry)
    runtime.register_executor(NoOpStepExecutor("service"))

    instance = runtime.create_instance("document.approval")
    completed = runtime.run_until_wait_or_complete(instance)

    assert completed.state == WorkflowState.COMPLETED
    assert completed.history == ("draft", "approve")
    assert completed.context.data["last_step"] == "approve"
