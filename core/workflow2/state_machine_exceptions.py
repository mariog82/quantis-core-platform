class StateMachineException(Exception):
    pass


class InvalidTransition(StateMachineException):
    pass


class GuardNotRegistered(StateMachineException):
    pass


class GuardRejectedTransition(StateMachineException):
    pass
