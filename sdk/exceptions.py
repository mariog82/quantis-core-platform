class SDKError(Exception):
    """Base SDK error."""


class SDKRequestError(SDKError):
    """Raised when an SDK request fails."""
