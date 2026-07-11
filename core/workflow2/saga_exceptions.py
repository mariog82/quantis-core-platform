class SagaException(Exception):
    pass


class SagaDefinitionInvalid(SagaException):
    pass


class SagaExecutionFailed(SagaException):
    pass


class SagaCompensationFailed(SagaException):
    pass
