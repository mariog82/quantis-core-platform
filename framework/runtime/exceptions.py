class RuntimeException(Exception):
    """Base runtime exception."""


class ModuleAlreadyRegistered(RuntimeException):
    """Raised when a module is registered more than once."""


class ModuleNotFound(RuntimeException):
    """Raised when a module does not exist in the registry."""


class CircularDependency(RuntimeException):
    """Raised when a dependency graph contains a cycle."""


class MissingDependency(RuntimeException):
    """Raised when a required dependency is not registered."""


class RuntimeStartupException(RuntimeException):
    """Raised when the runtime cannot start."""
