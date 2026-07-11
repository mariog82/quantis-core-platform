from dataclasses import asdict
from typing import Any

from core.workflow2.api_models import (
    CompleteHumanTaskRequest,
    CreateWorkflowInstanceRequest,
    WorkflowDefinitionResponse,
    WorkflowInstanceResponse,
)
from core.workflow2.human_task_service import HumanTaskService
from core.workflow2.human_tasks import HumanTaskId
from core.workflow2.registry import WorkflowRegistry
from core.workflow2.runtime import WorkflowRuntime


class WorkflowAPIService:
    def __init__(
        self,
        registry: WorkflowRegistry,
        runtime: WorkflowRuntime,
        human_tasks: HumanTaskService | None = None,
    ) -> None:
        self.registry = registry
        self.runtime = runtime
        self.human_tasks = human_tasks
        self._instances: dict[str, Any] = {}

    def list_definitions(self) -> list[dict[str, Any]]:
        definitions: list[dict[str, Any]] = []
        raw = getattr(self.registry, "_definitions", {})
        for definition in raw.values():
            definitions.append(
                asdict(WorkflowDefinitionResponse.from_definition(definition))
            )
        return sorted(
            definitions,
            key=lambda item: (item["workflow_id"], item["version"]),
        )

    def get_definition(
        self,
        workflow_id: str,
        version: int | None = None,
    ) -> dict[str, Any]:
        definition = (
            self.registry.latest(workflow_id)
            if version is None
            else self.registry.get(workflow_id, version)
        )
        return asdict(WorkflowDefinitionResponse.from_definition(definition))

    def create_instance(
        self,
        request: CreateWorkflowInstanceRequest,
    ) -> dict[str, Any]:
        instance = self.runtime.create_instance(
            workflow_id=request.workflow_id,
            version=request.version,
            context=request.to_context(),
        )
        self._instances[instance.instance_id.value] = instance
        return asdict(WorkflowInstanceResponse.from_instance(instance))

    def get_instance(self, instance_id: str) -> dict[str, Any]:
        instance = self._instances[instance_id]
        return asdict(WorkflowInstanceResponse.from_instance(instance))

    def run_instance(self, instance_id: str) -> dict[str, Any]:
        instance = self._instances[instance_id]
        updated = self.runtime.run_until_wait_or_complete(instance)
        self._instances[instance_id] = updated
        return asdict(WorkflowInstanceResponse.from_instance(updated))

    def complete_human_task(
        self,
        task_id: str,
        request: CompleteHumanTaskRequest,
    ) -> dict[str, Any]:
        if self.human_tasks is None:
            raise RuntimeError("Human task service is not configured")
        task = self.human_tasks.complete(
            HumanTaskId(task_id),
            request.user_id,
            request.result,
        )
        return {
            "task_id": task.task_id.value,
            "status": task.status.value,
            "assignee_id": task.assignee_id,
            "result": dict(task.result),
        }
