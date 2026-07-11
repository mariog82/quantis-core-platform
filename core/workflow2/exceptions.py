class WorkflowException(Exception):
    pass


class InvalidWorkflowDefinition(WorkflowException):
    pass


class DuplicateWorkflowDefinition(WorkflowException):
    pass


class WorkflowDefinitionNotFound(WorkflowException):
    pass
