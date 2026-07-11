from core.workflow2 import (
    InMemoryWorkflowRegistry,
    WorkflowContext,
    WorkflowDefinition,
    WorkflowRuntime,
    WorkflowState,
    WorkflowStepDefinition,
)


def test_runtime_creates_started_instance():
    registry = InMemoryWorkflowRegistry()
    registry.register(
        WorkflowDefinition(
            workflow_id="tenant.provisioning",
            version=1,
            name="Tenant Provisioning",
            initial_step_id="create",
            steps=(
                WorkflowStepDefinition(
                    step_id="create",
                    name="Create tenant",
                ),
            ),
        )
    )
    runtime = WorkflowRuntime(registry)

    instance = runtime.create_instance(
        "tenant.provisioning",
        context=WorkflowContext(
            data={"tenant_id": "t1"},
            tenant_id="t1",
        ),
    )

    assert instance.state == WorkflowState.RUNNING
    assert instance.current_step_id == "create"
    assert instance.context.tenant_id == "t1"
