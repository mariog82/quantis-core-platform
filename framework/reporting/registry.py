from framework.reporting.exceptions import ReportNotFound
from framework.reporting.models import ReportDefinition


class ReportRegistry:
    def __init__(self):
        self._reports: dict[str, ReportDefinition] = {}

    def register(self, definition: ReportDefinition) -> ReportDefinition:
        self._reports[definition.name] = definition
        return definition

    def get(self, name: str) -> ReportDefinition:
        if name not in self._reports:
            raise ReportNotFound(name)
        return self._reports[name]

    def exists(self, name: str) -> bool:
        return name in self._reports

    def list_reports(self) -> list[ReportDefinition]:
        return list(self._reports.values())

    def unregister(self, name: str) -> None:
        if name not in self._reports:
            raise ReportNotFound(name)
        self._reports.pop(name)
