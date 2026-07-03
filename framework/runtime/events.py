from dataclasses import dataclass


@dataclass
class RuntimeEvent:
    module: str


@dataclass
class ModuleRegistered(RuntimeEvent):
    pass


@dataclass
class ModuleStarted(RuntimeEvent):
    pass


@dataclass
class ModuleStopped(RuntimeEvent):
    pass


@dataclass
class KernelStarted(RuntimeEvent):
    pass


@dataclass
class KernelStopped(RuntimeEvent):
    pass