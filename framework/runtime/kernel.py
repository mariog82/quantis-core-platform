from framework.runtime.manager import RuntimeManager

from framework.runtime.state import RuntimeState


class RuntimeKernel:

    def __init__(self):

        self.state = RuntimeState.BOOTING

        self.manager = RuntimeManager()

    def initialize(self):

        self.state = RuntimeState.INITIALIZING

    def start(self):

        self.state = RuntimeState.RUNNING

    def stop(self):

        self.state = RuntimeState.STOPPED

    def health(self):

        return self.state.value