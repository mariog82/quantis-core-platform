import pytest

from core.workflow2 import (
    DuplicateWorkflowDefinition,
    InMemoryWorkflowRegistry,
    WorkflowContext,
    WorkflowDefinition,
    WorkflowDefinitionValidator,
    WorkflowId,
    WorkflowInstance,
    WorkflowState,
    WorkflowStepDefinition,
    WorkflowTransition,
    WorkflowVersion,
)


def make_definition(version: int = 1) -> WorkflowDefinition:
    return WorkflowDefinition(
        workflow_id="tenant.provisioning",
        version=version,
        name="Tenant Provisioning",
        initial_step_id="create-tenant",
        steps=(
            WorkflowStepDefinition("create-tenant", "Create tenant"),
            WorkflowStepDefinition("assign-license", "Assign license"),
        ),
        transitions=(
            WorkflowTransition("create-tenant", "assign-license"),
        ),
    )


def test_definition_and_instance_lifecycle():
    definition = make_definition()
    assert definition.step("create-tenant") is not None
    assert definition.outgoing("create-tenant")[0].target_step_id == "assign-license"

    instance = WorkflowInstance(
        workflow_id=WorkflowId(definition.workflow_id),
        workflow_version=WorkflowVersion(definition.version),
        context=WorkflowContext(data={"tenant_id": "t1"}, tenant_id="t1"),
    )
    completed = instance.start(definition.initial_step_id).move_to("assign-license").complete()

    assert completed.state == WorkflowState.COMPLETED
    assert completed.history == ("create-tenant", "assign-license")


def test_registry_and_validation():
    registry = InMemoryWorkflowRegistry()
    definition = make_definition()
    registry.register(definition)

    assert registry.latest("tenant.provisioning") == definition
    assert WorkflowDefinitionValidator().validate(definition).passed is True

    with pytest.raises(DuplicateWorkflowDefinition):
        registry.register(definition)
