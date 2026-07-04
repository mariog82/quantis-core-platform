class DashboardRuntimeError(Exception):
    """Base dashboard runtime error."""


class DashboardNotFound(DashboardRuntimeError):
    """Raised when a dashboard cannot be found."""


class WidgetNotFound(DashboardRuntimeError):
    """Raised when a widget cannot be found."""
