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
            return template.build_payload(context.filters)

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
        output = self.runtime.generate(template_key, ReportContext(filters=data))
        return output.content
