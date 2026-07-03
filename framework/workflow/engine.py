from framework.workflow.exceptions import WorkflowStepError
from framework.workflow.models import Workflow, WorkflowExecution, WorkflowExecutionStatus, WorkflowContext
from framework.workflow.registry import WorkflowRegistry


class WorkflowEngine:
    def __init__(self, registry: WorkflowRegistry | None = None):
        self.registry = registry or WorkflowRegistry()
        self.executions: list[WorkflowExecution] = []

    def register(self, workflow: Workflow) -> Workflow:
        return self.registry.register(workflow)

    def execute(self, workflow_name: str, context: WorkflowContext | None = None) -> WorkflowExecution:
        workflow = self.registry.get(workflow_name)
        execution = WorkflowExecution(
            workflow_id=workflow.id,
            status=WorkflowExecutionStatus.RUNNING,
            context=context or WorkflowContext(),
        )
        self.executions.append(execution)

        try:
            current_context = execution.context
            for step in workflow.steps:
                current_context = step.execute(current_context)
                execution.executed_steps.append(step.name)

            execution.context = current_context
            execution.status = WorkflowExecutionStatus.COMPLETED
            return execution

        except Exception as exc:
            execution.status = WorkflowExecutionStatus.FAILED
            execution.error = str(exc)
            raise WorkflowStepError(str(exc)) from exc
