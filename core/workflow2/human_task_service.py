from core.workflow2.human_task_repository import HumanTaskRepository
from core.workflow2.human_tasks import HumanTask, HumanTaskId


class HumanTaskService:
    def __init__(self, repository: HumanTaskRepository) -> None:
        self.repository = repository

    def create(self, task: HumanTask) -> HumanTask:
        return self.repository.save(task)

    def claim(self, task_id: HumanTaskId, user_id: str) -> HumanTask:
        task = self._require(task_id)
        return self.repository.save(task.claim(user_id))

    def start(self, task_id: HumanTaskId, user_id: str) -> HumanTask:
        task = self._require(task_id)
        return self.repository.save(task.start(user_id))

    def complete(
        self,
        task_id: HumanTaskId,
        user_id: str,
        result: dict | None = None,
    ) -> HumanTask:
        task = self._require(task_id)
        return self.repository.save(task.complete(user_id, result))

    def release(self, task_id: HumanTaskId, user_id: str) -> HumanTask:
        task = self._require(task_id)
        return self.repository.save(task.release(user_id))

    def delegate(
        self,
        task_id: HumanTaskId,
        from_user_id: str,
        to_user_id: str,
    ) -> HumanTask:
        task = self._require(task_id)
        return self.repository.save(
            task.delegate(from_user_id, to_user_id)
        )

    def _require(self, task_id: HumanTaskId) -> HumanTask:
        task = self.repository.get(task_id)
        if task is None:
            raise KeyError(task_id.value)
        return task
