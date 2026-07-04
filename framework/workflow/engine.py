from framework.workflow.models import Workflow, WorkflowContext, WorkflowExecution, WorkflowExecutionStatus


class WorkflowEngine:
    def __init__(self):
        self._workflows: dict[str, Workflow] = {}

    def register(self, workflow: Workflow) -> Workflow:
        self._workflows[workflow.name] = workflow
        return workflow

    def execute(self, workflow_name: str, context: WorkflowContext | None = None) -> WorkflowExecution:
        workflow = self._workflows[workflow_name]
        execution = WorkflowExecution(workflow_id=workflow.id, status=WorkflowExecutionStatus.RUNNING, context=context or WorkflowContext())
        current = execution.context
        for step in workflow.steps:
            current = step.execute(current)
        execution.context = current
        execution.status = WorkflowExecutionStatus.COMPLETED
        return execution
