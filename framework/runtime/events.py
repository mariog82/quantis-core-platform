from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class RuntimeEvent:
    event_type: str
    module_name: str | None = None
    metadata: dict = field(default_factory=dict)
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class KernelStarted(RuntimeEvent):
    def __init__(self, metadata: dict | None = None):
        super().__init__("kernel.started", metadata=metadata or {})


class KernelStopped(RuntimeEvent):
    def __init__(self, metadata: dict | None = None):
        super().__init__("kernel.stopped", metadata=metadata or {})


class ModuleRegistered(RuntimeEvent):
    def __init__(self, module_name: str, metadata: dict | None = None):
        super().__init__("module.registered", module_name=module_name, metadata=metadata or {})


class ModuleInitialized(RuntimeEvent):
    def __init__(self, module_name: str, metadata: dict | None = None):
        super().__init__("module.initialized", module_name=module_name, metadata=metadata or {})


class ModuleStarted(RuntimeEvent):
    def __init__(self, module_name: str, metadata: dict | None = None):
        super().__init__("module.started", module_name=module_name, metadata=metadata or {})


class ModuleStopped(RuntimeEvent):
    def __init__(self, module_name: str, metadata: dict | None = None):
        super().__init__("module.stopped", module_name=module_name, metadata=metadata or {})


class ModuleFailed(RuntimeEvent):
    def __init__(self, module_name: str, metadata: dict | None = None):
        super().__init__("module.failed", module_name=module_name, metadata=metadata or {})
