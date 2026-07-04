from framework.reporting.exceptions import ReportRendererNotFound
from framework.reporting.models import Report, ReportContext, ReportFormat, ReportOutput
from framework.reporting.registry import ReportRegistry
from framework.reporting.renderer import ReportRenderer, TextReportRenderer


class ReportingRuntime:
    def __init__(self, registry: ReportRegistry | None = None):
        self.registry = registry or ReportRegistry()
        self.renderers: dict[ReportFormat, ReportRenderer] = {}
        self.register_renderer(TextReportRenderer())

    def register_renderer(self, renderer: ReportRenderer) -> ReportRenderer:
        self.renderers[renderer.format] = renderer
        return renderer

    def register(self, definition):
        return self.registry.register(definition)

    def generate(
        self,
        name: str,
        context: ReportContext | None = None,
        report_format: ReportFormat | None = None,
    ) -> ReportOutput:
        definition = self.registry.get(name)
        context = context or ReportContext()
        selected_format = report_format or definition.default_format
        renderer = self.renderers.get(selected_format)
        if renderer is None:
            raise ReportRendererNotFound(selected_format.value)
        payload = definition.provider(context) if definition.provider else {}
        report = Report(definition=definition, payload=payload, context=context)
        return renderer.render(report)
