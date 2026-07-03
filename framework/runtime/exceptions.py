class RuntimeException(Exception): pass
class ModuleAlreadyRegistered(RuntimeException): pass
class ModuleNotFound(RuntimeException): pass
class CircularDependency(RuntimeException): pass
class MissingDependency(RuntimeException): pass
class RuntimeStartupException(RuntimeException): pass
