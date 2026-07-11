from dataclasses import dataclass, field
from typing import Any, Callable

from core.workflow2.definition import WorkflowDefinition, WorkflowTransition
from core.workflow2.instance import WorkflowInstance, WorkflowState


Guard = Callable[[WorkflowInstance], bool]


@dataclass(frozen=True)
class StateTransitionRule:
    source_step_id: str
    target_step_id: str
    guard_name: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class StateMachineDecision:
    allowed: bool
    target_step_id: str | None = None
    reason: str | None = None


class WorkflowStateMachine:
    def __init__(self) -> None:
        self._guards: dict[str, Guard] = {}

    def register_guard(self, name: str, guard: Guard) -> None:
        self._guards[name] = guard

    def can_transition(
        self,
        definition: WorkflowDefinition,
        instance: WorkflowInstance,
        target_step_id: str,
    ) -> StateMachineDecision:
        if instance.state != WorkflowState.RUNNING:
            return StateMachineDecision(
                allowed=False,
                reason=f"workflow state is {instance.state.value}",
            )

        if instance.current_step_id is None:
            return StateMachineDecision(
                allowed=False,
                reason="workflow has no current step",
            )

        transition = self._find_transition(
            definition,
            instance.current_step_id,
            target_step_id,
        )
        if transition is None:
            return StateMachineDecision(
                allowed=False,
                reason="transition is not defined",
            )

        if transition.condition:
            guard = self._guards.get(transition.condition)
            if guard is None:
                return StateMachineDecision(
                    allowed=False,
                    reason=f"guard not registered: {transition.condition}",
                )
            if not guard(instance):
                return StateMachineDecision(
                    allowed=False,
                    reason=f"guard rejected transition: {transition.condition}",
                )

        return StateMachineDecision(
            allowed=True,
            target_step_id=target_step_id,
        )

    def transition(
        self,
        definition: WorkflowDefinition,
        instance: WorkflowInstance,
        target_step_id: str,
    ) -> WorkflowInstance:
        decision = self.can_transition(
            definition,
            instance,
            target_step_id,
        )
        if not decision.allowed:
            raise ValueError(decision.reason or "transition rejected")
        return instance.move_to(target_step_id)

    def available_transitions(
        self,
        definition: WorkflowDefinition,
        instance: WorkflowInstance,
    ) -> tuple[WorkflowTransition, ...]:
        if instance.current_step_id is None:
            return ()

        available: list[WorkflowTransition] = []
        for transition in definition.outgoing(instance.current_step_id):
            if transition.condition is None:
                available.append(transition)
                continue

            guard = self._guards.get(transition.condition)
            if guard is not None and guard(instance):
                available.append(transition)

        return tuple(available)

    @staticmethod
    def _find_transition(
        definition: WorkflowDefinition,
        source_step_id: str,
        target_step_id: str,
    ) -> WorkflowTransition | None:
        return next(
            (
                transition
                for transition in definition.transitions
                if transition.source_step_id == source_step_id
                and transition.target_step_id == target_step_id
            ),
            None,
        )
