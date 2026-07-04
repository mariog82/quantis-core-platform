from modules.reporting.template import ReportTemplate


class ReportCatalog:
    def __init__(self):
        self._templates: dict[str, ReportTemplate] = {}

    def register(self, template: ReportTemplate) -> ReportTemplate:
        self._templates[template.key] = template
        return template

    def get(self, key: str) -> ReportTemplate:
        return self._templates[key]

    def exists(self, key: str) -> bool:
        return key in self._templates

    def list_templates(self) -> list[ReportTemplate]:
        return list(self._templates.values())
