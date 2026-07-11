from dataclasses import dataclass, field

from core.workflow2.definition import WorkflowDefinition


@dataclass(frozen=True)
class WorkflowValidationIssue:
    code: str
    message: str


@dataclass
class WorkflowValidationReport:
    issues: list[WorkflowValidationIssue] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.issues

    def add(self, code: str, message: str) -> None:
        self.issues.append(WorkflowValidationIssue(code=code, message=message))


WorkflowValidationIssue.__test__ = False
WorkflowValidationReport.__test__ = False


class WorkflowDefinitionValidator:
    def validate(self, definition: WorkflowDefinition) -> WorkflowValidationReport:
        report = WorkflowValidationReport()
        step_ids = [step.step_id for step in definition.steps]

        if not definition.workflow_id.strip():
            report.add("EMPTY_WORKFLOW_ID", "Workflow id must not be empty.")
        if definition.version < 1:
            report.add("INVALID_VERSION", "Workflow version must be >= 1.")
        if not step_ids:
            report.add("NO_STEPS", "Workflow must contain at least one step.")
        if len(step_ids) != len(set(step_ids)):
            report.add("DUPLICATE_STEP_ID", "Workflow step ids must be unique.")
        if definition.initial_step_id not in step_ids:
            report.add("INVALID_INITIAL_STEP", "Initial step must reference a defined step.")

        for transition in definition.transitions:
            if transition.source_step_id not in step_ids:
                report.add("UNKNOWN_TRANSITION_SOURCE", transition.source_step_id)
            if transition.target_step_id not in step_ids:
                report.add("UNKNOWN_TRANSITION_TARGET", transition.target_step_id)

        return report
