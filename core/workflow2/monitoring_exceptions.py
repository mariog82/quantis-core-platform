class WorkflowMonitoringException(Exception):
    pass


class WorkflowMonitoringEventInvalid(WorkflowMonitoringException):
    pass


class WorkflowMonitoringSinkUnavailable(WorkflowMonitoringException):
    pass
