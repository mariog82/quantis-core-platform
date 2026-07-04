from framework.reporting.models import ReportContext, ReportDefinition, ReportOutput
from framework.reporting.renderer import TextReportRenderer


class ReportingRuntime:
    def __init__(self):
        self._definitions: dict[str, ReportDefinition] = {}
        self.renderer = TextReportRenderer()

    def register(self, definition: ReportDefinition) -> ReportDefinition:
        self._definitions[definition.name] = definition
        return definition

    def generate(self, name: str, context: ReportContext | None = None) -> ReportOutput:
        definition = self._definitions[name]
        ctx = context or ReportContext()
        payload = definition.provider(ctx) if definition.provider else {}
        return self.renderer.render(definition, payload)
