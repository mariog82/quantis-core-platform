from __future__ import annotations

from typing import Callable

from framework.contracts.module import BaseModule
from framework.runtime.exceptions import ModuleAlreadyRegistered, ModuleNotFound
from framework.runtime.health import HealthReport, ModuleHealth
from framework.runtime.state import ModuleState


class ModuleRegistry:
    def __init__(self):
        self._modules: dict[str, BaseModule] = {}
        self._states: dict[str, ModuleState] = {}

    def register(self, module: BaseModule) -> BaseModule:
        name = module.manifest.name
        if name in self._modules:
            raise ModuleAlreadyRegistered(name)
        self._modules[name] = module
        self._states[name] = ModuleState.REGISTERED
        return module

    def unregister(self, name: str) -> None:
        if name not in self._modules:
            raise ModuleNotFound(name)
        self._modules.pop(name)
        self._states.pop(name, None)

    def get(self, name: str) -> BaseModule:
        if name not in self._modules:
            raise ModuleNotFound(name)
        return self._modules[name]

    def exists(self, name: str) -> bool:
        return name in self._modules

    def list(self) -> list[BaseModule]:
        return list(self._modules.values())

    def state(self, name: str) -> ModuleState:
        if name not in self._states:
            raise ModuleNotFound(name)
        return self._states[name]

    def set_state(self, name: str, state: ModuleState) -> None:
        if name not in self._modules:
            raise ModuleNotFound(name)
        self._states[name] = state

    def find(self, predicate: Callable[[BaseModule], bool]) -> list[BaseModule]:
        return [module for module in self._modules.values() if predicate(module)]

    def find_by_capability(self, capability: str) -> list[BaseModule]:
        return [
            module
            for module in self._modules.values()
            if capability in getattr(module.manifest, "capabilities", [])
        ]

    def health(self) -> list[HealthReport]:
        reports = []
        for module in self._modules.values():
            name = module.manifest.name
            try:
                details = module.health()
                status = (
                    ModuleHealth.READY
                    if self._states[name] in {ModuleState.RUNNING, ModuleState.READY}
                    else ModuleHealth.UNKNOWN
                )
                reports.append(HealthReport(status=status, component=name, details=details))
            except Exception as exc:
                reports.append(
                    HealthReport(
                        status=ModuleHealth.FAILED,
                        component=name,
                        details={"error": str(exc)},
                    )
                )
        return reports
