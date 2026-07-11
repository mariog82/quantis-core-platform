class HumanTaskException(Exception):
    pass


class HumanTaskNotFound(HumanTaskException):
    pass


class HumanTaskPermissionDenied(HumanTaskException):
    pass


class InvalidHumanTaskState(HumanTaskException):
    pass
