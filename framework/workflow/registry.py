from framework.workflow.exceptions import WorkflowNotFound
from framework.workflow.models import Workflow


class WorkflowRegistry:
    def __init__(self):
        self._workflows: dict[str, Workflow] = {}

    def register(self, workflow: Workflow) -> Workflow:
        self._workflows[workflow.name] = workflow
        return workflow

    def get(self, name: str) -> Workflow:
        if name not in self._workflows:
            raise WorkflowNotFound(name)
        return self._workflows[name]

    def exists(self, name: str) -> bool:
        return name in self._workflows

    def list_workflows(self) -> list[Workflow]:
        return list(self._workflows.values())

    def unregister(self, name: str) -> None:
        if name not in self._workflows:
            raise WorkflowNotFound(name)
        self._workflows.pop(name)
