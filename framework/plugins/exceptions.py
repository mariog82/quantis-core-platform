class PluginRuntimeError(Exception): pass
class PluginAlreadyRegistered(PluginRuntimeError): pass
class PluginNotFound(PluginRuntimeError): pass
class ExtensionPointNotFound(PluginRuntimeError): pass
