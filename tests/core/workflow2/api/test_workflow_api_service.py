from core.workflow2 import (
    InMemoryWorkflowRegistry,
    NoOpStepExecutor,
    WorkflowDefinition,
    WorkflowRuntime,
    WorkflowStepDefinition,
)
from core.workflow2.api_models import CreateWorkflowInstanceRequest
from core.workflow2.api_service import WorkflowAPIService


def test_api_service_creates_and_runs_instance():
    registry = InMemoryWorkflowRegistry()
    registry.register(
        WorkflowDefinition(
            workflow_id="simple.flow",
            version=1,
            name="Simple Flow",
            initial_step_id="run",
            steps=(
                WorkflowStepDefinition("run", "Run"),
            ),
        )
    )
    runtime = WorkflowRuntime(registry)
    runtime.register_executor(NoOpStepExecutor())
    service = WorkflowAPIService(registry, runtime)

    created = service.create_instance(
        CreateWorkflowInstanceRequest(
            workflow_id="simple.flow",
            context={"value": 1},
        )
    )
    completed = service.run_instance(created["instance_id"])

    assert created["state"] == "running"
    assert completed["state"] == "completed"
