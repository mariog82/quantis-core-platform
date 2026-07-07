class AdapterError(Exception):
    """Base adapter error."""

class AdapterNotFound(AdapterError):
    """Raised when an adapter cannot be found."""

class AdapterAlreadyRegistered(AdapterError):
    """Raised when an adapter is registered more than once."""

class AdapterExecutionError(AdapterError):
    """Raised when an adapter execution fails."""
