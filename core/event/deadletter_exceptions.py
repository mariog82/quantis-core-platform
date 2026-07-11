class DeadLetterException(Exception):
    pass


class DeadLetterNotFoundException(DeadLetterException):
    pass


class DeadLetterReplayException(DeadLetterException):
    pass


class DeadLetterPersistenceException(DeadLetterException):
    pass
