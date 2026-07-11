class WorkflowSDKException(Exception):
    pass


class WorkflowSDKNotFound(WorkflowSDKException):
    pass


class WorkflowSDKTransportError(WorkflowSDKException):
    pass
