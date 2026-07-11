class DispatcherException(Exception):
    pass


class DispatchFailedException(DispatcherException):
    pass


class MiddlewareExecutionException(DispatcherException):
    pass


class InterceptorExecutionException(DispatcherException):
    pass
