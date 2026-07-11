from datetime import datetime, timezone
from typing import Protocol

from core.workflow2.timers import (
    TimerStatus,
    WorkflowTimer,
    WorkflowTimerId,
)


class WorkflowTimerRepository(Protocol):
    def save(self, timer: WorkflowTimer) -> WorkflowTimer:
        ...

    def get(self, timer_id: WorkflowTimerId) -> WorkflowTimer | None:
        ...

    def due(self, now: datetime | None = None) -> list[WorkflowTimer]:
        ...

    def list_for_instance(self, workflow_instance_id: str) -> list[WorkflowTimer]:
        ...


class InMemoryWorkflowTimerRepository:
    def __init__(self) -> None:
        self._timers: dict[str, WorkflowTimer] = {}

    def save(self, timer: WorkflowTimer) -> WorkflowTimer:
        self._timers[timer.timer_id.value] = timer
        return timer

    def get(self, timer_id: WorkflowTimerId) -> WorkflowTimer | None:
        return self._timers.get(timer_id.value)

    def due(self, now: datetime | None = None) -> list[WorkflowTimer]:
        current = now or datetime.now(timezone.utc)
        return [
            timer
            for timer in self._timers.values()
            if timer.is_due(current)
        ]

    def list_for_instance(self, workflow_instance_id: str) -> list[WorkflowTimer]:
        return [
            timer
            for timer in self._timers.values()
            if timer.workflow_instance_id == workflow_instance_id
        ]


class WorkflowScheduler:
    def __init__(self, repository: WorkflowTimerRepository) -> None:
        self.repository = repository

    def schedule(self, timer: WorkflowTimer) -> WorkflowTimer:
        return self.repository.save(timer)

    def cancel(self, timer_id: WorkflowTimerId) -> WorkflowTimer:
        timer = self._require(timer_id)
        cancelled = timer.cancel()
        return self.repository.save(cancelled)

    def fire_due(self, now: datetime | None = None) -> list[WorkflowTimer]:
        current = now or datetime.now(timezone.utc)
        fired: list[WorkflowTimer] = []

        for timer in self.repository.due(current):
            updated = timer.fire(current)
            self.repository.save(updated)
            fired.append(updated)

        return fired

    def pending_for_instance(self, workflow_instance_id: str) -> list[WorkflowTimer]:
        return [
            timer
            for timer in self.repository.list_for_instance(workflow_instance_id)
            if timer.status == TimerStatus.SCHEDULED
        ]

    def _require(self, timer_id: WorkflowTimerId) -> WorkflowTimer:
        timer = self.repository.get(timer_id)
        if timer is None:
            raise KeyError(timer_id.value)
        return timer
