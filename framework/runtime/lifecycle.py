from framework.runtime.state import ModuleState


class LifecycleManager:

    def initialize(self, module):

        module.state = ModuleState.INITIALIZED

    def start(self, module):

        module.state = ModuleState.RUNNING

    def stop(self, module):

        module.state = ModuleState.STOPPED

    def disable(self, module):

        module.state = ModuleState.DISABLED