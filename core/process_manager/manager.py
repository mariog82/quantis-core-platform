from dataclasses import dataclass, field, replace
from enum import Enum
from typing import Any
from uuid import uuid4


class ProcessStatus(str, Enum):
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    COMPENSATED = "compensated"


@dataclass(frozen=True)
class ProcessInstance:
    process_type: str
    state: dict[str, Any]
    process_id: str = field(default_factory=lambda: str(uuid4()))
    status: ProcessStatus = ProcessStatus.RUNNING
    current_step: str | None = None


class ProcessManager:
    def __init__(self) -> None:
        self._instances: dict[str, ProcessInstance] = {}

    def start(
        self,
        process_type: str,
        state: dict[str, Any] | None = None,
    ) -> ProcessInstance:
        instance = ProcessInstance(
            process_type=process_type,
            state=dict(state or {}),
        )
        self._instances[instance.process_id] = instance
        return instance

    def advance(
        self,
        process_id: str,
        step: str,
        state_updates: dict[str, Any] | None = None,
    ) -> ProcessInstance:
        instance = self._instances[process_id]
        state = dict(instance.state)
        state.update(state_updates or {})
        updated = replace(
            instance,
            state=state,
            current_step=step,
        )
        self._instances[process_id] = updated
        return updated

    def complete(self, process_id: str) -> ProcessInstance:
        instance = self._instances[process_id]
        updated = replace(instance, status=ProcessStatus.COMPLETED)
        self._instances[process_id] = updated
        return updated

    def fail(self, process_id: str) -> ProcessInstance:
        instance = self._instances[process_id]
        updated = replace(instance, status=ProcessStatus.FAILED)
        self._instances[process_id] = updated
        return updated

    def get(self, process_id: str) -> ProcessInstance | None:
        return self._instances.get(process_id)
