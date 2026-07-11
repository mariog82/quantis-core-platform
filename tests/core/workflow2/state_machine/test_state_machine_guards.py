from core.workflow2 import (
    WorkflowContext,
    WorkflowDefinition,
    WorkflowId,
    WorkflowInstance,
    WorkflowStateMachine,
    WorkflowStepDefinition,
    WorkflowTransition,
    WorkflowVersion,
)


def test_guard_controls_transition():
    definition = WorkflowDefinition(
        workflow_id="vote.lifecycle",
        version=1,
        name="Vote Lifecycle",
        initial_step_id="open",
        steps=(
            WorkflowStepDefinition("open", "Open"),
            WorkflowStepDefinition("closed", "Closed"),
        ),
        transitions=(
            WorkflowTransition(
                "open",
                "closed",
                condition="quorum-reached",
            ),
        ),
    )
    instance = WorkflowInstance(
        workflow_id=WorkflowId("vote.lifecycle"),
        workflow_version=WorkflowVersion(1),
        context=WorkflowContext(data={"quorum": True}),
    ).start("open")

    machine = WorkflowStateMachine()
    machine.register_guard(
        "quorum-reached",
        lambda current: bool(current.context.data.get("quorum")),
    )

    decision = machine.can_transition(
        definition,
        instance,
        "closed",
    )

    assert decision.allowed is True
    assert decision.target_step_id == "closed"
