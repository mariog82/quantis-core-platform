class RuntimeException(Exception):
    pass


class ModuleAlreadyRegistered(RuntimeException):
    pass


class ModuleNotFound(RuntimeException):
    pass


class DependencyError(RuntimeException):
    pass