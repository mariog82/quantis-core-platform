from framework.runtime.registry import ModuleRegistry
from framework.runtime.lifecycle import LifecycleManager


class RuntimeManager:

    def __init__(self):

        self.registry = ModuleRegistry()

        self.lifecycle = LifecycleManager()