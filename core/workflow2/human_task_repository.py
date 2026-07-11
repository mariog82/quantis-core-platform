from typing import Protocol

from core.workflow2.human_tasks import HumanTask, HumanTaskId, HumanTaskStatus


class HumanTaskRepository(Protocol):
    def save(self, task: HumanTask) -> HumanTask:
        ...

    def get(self, task_id: HumanTaskId) -> HumanTask | None:
        ...

    def list_for_assignee(self, user_id: str) -> list[HumanTask]:
        ...

    def list_open(self) -> list[HumanTask]:
        ...


class InMemoryHumanTaskRepository:
    def __init__(self) -> None:
        self._tasks: dict[str, HumanTask] = {}

    def save(self, task: HumanTask) -> HumanTask:
        self._tasks[task.task_id.value] = task
        return task

    def get(self, task_id: HumanTaskId) -> HumanTask | None:
        return self._tasks.get(task_id.value)

    def list_for_assignee(self, user_id: str) -> list[HumanTask]:
        return [
            task
            for task in self._tasks.values()
            if task.assignee_id == user_id
        ]

    def list_open(self) -> list[HumanTask]:
        terminal = {
            HumanTaskStatus.COMPLETED,
            HumanTaskStatus.CANCELLED,
            HumanTaskStatus.EXPIRED,
        }
        return [
            task
            for task in self._tasks.values()
            if task.status not in terminal
        ]
