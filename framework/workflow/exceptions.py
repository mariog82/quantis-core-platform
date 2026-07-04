class WorkflowRuntimeError(Exception):
    """Base workflow runtime error."""


class WorkflowNotFound(WorkflowRuntimeError):
    """Raised when a workflow cannot be found."""


class WorkflowStepError(WorkflowRuntimeError):
    """Raised when a workflow step fails."""
