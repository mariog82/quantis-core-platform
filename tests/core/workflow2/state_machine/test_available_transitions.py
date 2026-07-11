from core.workflow2 import (
    WorkflowDefinition,
    WorkflowId,
    WorkflowInstance,
    WorkflowStateMachine,
    WorkflowStepDefinition,
    WorkflowTransition,
    WorkflowVersion,
)


def test_available_transitions_filters_failed_guards():
    definition = WorkflowDefinition(
        workflow_id="approval",
        version=1,
        name="Approval",
        initial_step_id="review",
        steps=(
            WorkflowStepDefinition("review", "Review"),
            WorkflowStepDefinition("approve", "Approve"),
            WorkflowStepDefinition("reject", "Reject"),
        ),
        transitions=(
            WorkflowTransition("review", "approve", condition="can-approve"),
            WorkflowTransition("review", "reject"),
        ),
    )
    instance = WorkflowInstance(
        workflow_id=WorkflowId("approval"),
        workflow_version=WorkflowVersion(1),
    ).start("review")

    machine = WorkflowStateMachine()
    machine.register_guard("can-approve", lambda current: False)

    available = machine.available_transitions(definition, instance)

    assert len(available) == 1
    assert available[0].target_step_id == "reject"
