class ReportingRuntimeError(Exception):
    """Base reporting runtime error."""


class ReportNotFound(ReportingRuntimeError):
    """Raised when a report definition cannot be found."""


class ReportRendererNotFound(ReportingRuntimeError):
    """Raised when no renderer is registered for a report format."""
