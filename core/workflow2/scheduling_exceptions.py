class WorkflowSchedulingException(Exception):
    pass


class WorkflowTimerNotFound(WorkflowSchedulingException):
    pass


class WorkflowTimerNotDue(WorkflowSchedulingException):
    pass


class InvalidWorkflowTimerState(WorkflowSchedulingException):
    pass
