from framework.reporting.models import ReportDefinition, ReportFormat, ReportOutput


class TextReportRenderer:
    format = ReportFormat.TEXT

    def render(self, definition: ReportDefinition, payload: dict) -> ReportOutput:
        lines = [definition.title, ""]
        for key, value in payload.items():
            lines.append(f"{key}: {value}")
        return ReportOutput(definition.name, ReportFormat.TEXT, "\n".join(lines).encode(), "text/plain")
