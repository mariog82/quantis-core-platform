from abc import ABC, abstractmethod
from enum import Enum
from framework.adapters.context import AdapterContext
from framework.adapters.metadata import AdapterMetadata
from framework.adapters.result import AdapterResult

class AdapterLifecycleState(str, Enum):
    CREATED = "created"
    CONFIGURED = "configured"
    STARTED = "started"
    STOPPED = "stopped"

class Adapter(ABC):
    metadata: AdapterMetadata

    def __init__(self):
        self.state = AdapterLifecycleState.CREATED
        self.context: AdapterContext | None = None

    def configure(self, context: AdapterContext) -> None:
        self.context = context
        self.state = AdapterLifecycleState.CONFIGURED

    def start(self) -> None:
        self.state = AdapterLifecycleState.STARTED

    def stop(self) -> None:
        self.state = AdapterLifecycleState.STOPPED

    @abstractmethod
    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        raise NotImplementedError
