import pytest

from core.workflow2 import (
    WorkflowDefinition,
    WorkflowId,
    WorkflowInstance,
    WorkflowStateMachine,
    WorkflowStepDefinition,
    WorkflowTransition,
    WorkflowVersion,
)


def make_definition() -> WorkflowDefinition:
    return WorkflowDefinition(
        workflow_id="document.approval",
        version=1,
        name="Document Approval",
        initial_step_id="draft",
        steps=(
            WorkflowStepDefinition("draft", "Draft"),
            WorkflowStepDefinition("review", "Review"),
            WorkflowStepDefinition("approved", "Approved"),
        ),
        transitions=(
            WorkflowTransition("draft", "review"),
            WorkflowTransition(
                "review",
                "approved",
                condition="is-approved",
            ),
        ),
    )


def make_instance() -> WorkflowInstance:
    return WorkflowInstance(
        workflow_id=WorkflowId("document.approval"),
        workflow_version=WorkflowVersion(1),
    ).start("draft")


def test_state_machine_allows_defined_transition():
    machine = WorkflowStateMachine()
    instance = make_instance()

    moved = machine.transition(
        make_definition(),
        instance,
        "review",
    )

    assert moved.current_step_id == "review"


def test_state_machine_rejects_undefined_transition():
    machine = WorkflowStateMachine()

    with pytest.raises(ValueError):
        machine.transition(
            make_definition(),
            make_instance(),
            "approved",
        )
