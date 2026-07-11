class WorkflowRuntimeException(Exception):
    pass


class StepExecutorNotFound(WorkflowRuntimeException):
    pass


class WorkflowExecutionLimitExceeded(WorkflowRuntimeException):
    pass
