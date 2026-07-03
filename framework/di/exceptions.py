class DependencyRegistrationError(Exception):
    """Raised when dependency registration is invalid."""


class DependencyNotFound(Exception):
    """Raised when a dependency cannot be resolved."""
