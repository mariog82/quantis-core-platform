from typing import Any, Protocol

from core.workflow2.api_models import (
    CompleteHumanTaskRequest,
    CreateWorkflowInstanceRequest,
)
from core.workflow2.api_service import WorkflowAPIService


class WorkflowTransport(Protocol):
    def request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
    ) -> dict[str, Any] | list[dict[str, Any]]:
        ...


class InProcessWorkflowTransport:
    def __init__(self, service: WorkflowAPIService) -> None:
        self.service = service

    def request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
    ) -> dict[str, Any] | list[dict[str, Any]]:
        parts = [part for part in path.split("/") if part]

        if method == "GET" and parts == ["workflows"]:
            return self.service.list_definitions()

        if method == "GET" and len(parts) == 2 and parts[0] == "workflows":
            return self.service.get_definition(parts[1])

        if method == "POST" and parts == ["workflow-instances"]:
            return self.service.create_instance(
                CreateWorkflowInstanceRequest(**(payload or {}))
            )

        if (
            method == "GET"
            and len(parts) == 2
            and parts[0] == "workflow-instances"
        ):
            return self.service.get_instance(parts[1])

        if (
            method == "POST"
            and len(parts) == 3
            and parts[0] == "workflow-instances"
            and parts[2] == "run"
        ):
            return self.service.run_instance(parts[1])

        if (
            method == "POST"
            and len(parts) == 3
            and parts[0] == "human-tasks"
            and parts[2] == "complete"
        ):
            return self.service.complete_human_task(
                parts[1],
                CompleteHumanTaskRequest(**(payload or {})),
            )

        raise KeyError(f"Unsupported route: {method} {path}")
