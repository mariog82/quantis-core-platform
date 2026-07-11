from typing import Protocol

from core.workflow2.definition import WorkflowDefinition
from core.workflow2.exceptions import DuplicateWorkflowDefinition, WorkflowDefinitionNotFound


class WorkflowRegistry(Protocol):
    def register(self, definition: WorkflowDefinition) -> WorkflowDefinition: ...
    def get(self, workflow_id: str, version: int) -> WorkflowDefinition: ...
    def latest(self, workflow_id: str) -> WorkflowDefinition: ...
    def list_versions(self, workflow_id: str) -> list[int]: ...


class InMemoryWorkflowRegistry:
    def __init__(self) -> None:
        self._definitions: dict[tuple[str, int], WorkflowDefinition] = {}

    def register(self, definition: WorkflowDefinition) -> WorkflowDefinition:
        key = (definition.workflow_id, definition.version)
        if key in self._definitions:
            raise DuplicateWorkflowDefinition(f"{definition.workflow_id}@{definition.version}")
        self._definitions[key] = definition
        return definition

    def get(self, workflow_id: str, version: int) -> WorkflowDefinition:
        key = (workflow_id, version)
        if key not in self._definitions:
            raise WorkflowDefinitionNotFound(f"{workflow_id}@{version}")
        return self._definitions[key]

    def latest(self, workflow_id: str) -> WorkflowDefinition:
        versions = self.list_versions(workflow_id)
        if not versions:
            raise WorkflowDefinitionNotFound(workflow_id)
        return self.get(workflow_id, max(versions))

    def list_versions(self, workflow_id: str) -> list[int]:
        return sorted(
            version
            for current_workflow_id, version in self._definitions
            if current_workflow_id == workflow_id
        )
