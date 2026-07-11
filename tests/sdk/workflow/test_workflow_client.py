from core.workflow2 import (
    InMemoryWorkflowRegistry,
    NoOpStepExecutor,
    WorkflowDefinition,
    WorkflowRuntime,
    WorkflowStepDefinition,
)
from core.workflow2.api_service import WorkflowAPIService
from sdk.workflow import (
    InProcessWorkflowTransport,
    WorkflowClient,
)


def test_workflow_client_executes_in_process_api():
    registry = InMemoryWorkflowRegistry()
    registry.register(
        WorkflowDefinition(
            workflow_id="sdk.flow",
            version=1,
            name="SDK Flow",
            initial_step_id="step",
            steps=(
                WorkflowStepDefinition("step", "Step"),
            ),
        )
    )
    runtime = WorkflowRuntime(registry)
    runtime.register_executor(NoOpStepExecutor())

    client = WorkflowClient(
        InProcessWorkflowTransport(
            WorkflowAPIService(registry, runtime)
        )
    )

    workflows = client.list_workflows()
    created = client.create_instance("sdk.flow")
    completed = client.run_instance(created["instance_id"])

    assert workflows[0]["workflow_id"] == "sdk.flow"
    assert completed["state"] == "completed"
