from framework.reporting import ReportContext, ReportDefinition, ReportId, ReportingRuntime
from modules.reporting.catalog import ReportCatalog
from modules.reporting.template import ReportTemplate


class ReportingModuleService:
    def __init__(
        self,
        catalog: ReportCatalog | None = None,
        runtime: ReportingRuntime | None = None,
    ):
        self.catalog = catalog or ReportCatalog()
        self.runtime = runtime or ReportingRuntime()

    def register_template(self, template: ReportTemplate) -> ReportTemplate:
        self.catalog.register(template)

        def provider(context: ReportContext) -> dict:
            source_data = getattr(context, "filters", None)
            if source_data is None:
                source_data = getattr(context, "metadata", {})
            return template.build_payload(source_data)

        self.runtime.register(
            ReportDefinition(
                id=ReportId(),
                name=template.key,
                title=template.title,
                provider=provider,
            )
        )
        return template

    def generate(self, template_key: str, data: dict) -> bytes:
        context = ReportContext()
        if hasattr(context, "filters"):
            context.filters = data
        else:
            context.metadata = data
        output = self.runtime.generate(template_key, context)
        return output.content
