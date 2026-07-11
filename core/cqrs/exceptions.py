class CQRSException(Exception):
    pass


class CommandHandlerNotFound(CQRSException):
    pass


class QueryHandlerNotFound(CQRSException):
    pass


class DuplicateHandlerRegistration(CQRSException):
    pass
