from typing import Any

from sdk.workflow.config import WorkflowSDKConfig
from sdk.workflow.transport import WorkflowTransport


class WorkflowClient:
    def __init__(
        self,
        transport: WorkflowTransport,
        config: WorkflowSDKConfig | None = None,
    ) -> None:
        self.transport = transport
        self.config = config or WorkflowSDKConfig()

    def list_workflows(self) -> list[dict[str, Any]]:
        result = self.transport.request("GET", "/workflows")
        assert isinstance(result, list)
        return result

    def get_workflow(self, workflow_id: str) -> dict[str, Any]:
        result = self.transport.request(
            "GET",
            f"/workflows/{workflow_id}",
        )
        assert isinstance(result, dict)
        return result

    def create_instance(
        self,
        workflow_id: str,
        *,
        version: int | None = None,
        context: dict[str, Any] | None = None,
        tenant_id: str | None = None,
        correlation_id: str | None = None,
        user_id: str | None = None,
    ) -> dict[str, Any]:
        result = self.transport.request(
            "POST",
            "/workflow-instances",
            {
                "workflow_id": workflow_id,
                "version": version,
                "context": dict(context or {}),
                "tenant_id": tenant_id or self.config.tenant_id,
                "correlation_id": correlation_id,
                "user_id": user_id,
            },
        )
        assert isinstance(result, dict)
        return result

    def get_instance(self, instance_id: str) -> dict[str, Any]:
        result = self.transport.request(
            "GET",
            f"/workflow-instances/{instance_id}",
        )
        assert isinstance(result, dict)
        return result

    def run_instance(self, instance_id: str) -> dict[str, Any]:
        result = self.transport.request(
            "POST",
            f"/workflow-instances/{instance_id}/run",
        )
        assert isinstance(result, dict)
        return result

    def complete_human_task(
        self,
        task_id: str,
        user_id: str,
        result_data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        result = self.transport.request(
            "POST",
            f"/human-tasks/{task_id}/complete",
            {
                "user_id": user_id,
                "result": dict(result_data or {}),
            },
        )
        assert isinstance(result, dict)
        return result
