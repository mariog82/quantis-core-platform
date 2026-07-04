class PluginRuntimeError(Exception):
    """Base plugin runtime error."""


class PluginAlreadyRegistered(PluginRuntimeError):
    """Raised when a plugin is registered more than once."""


class PluginNotFound(PluginRuntimeError):
    """Raised when a plugin cannot be found."""


class ExtensionPointNotFound(PluginRuntimeError):
    """Raised when an extension point cannot be found."""
