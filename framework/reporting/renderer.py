from abc import ABC, abstractmethod

from framework.reporting.models import Report, ReportFormat, ReportOutput


class ReportRenderer(ABC):
    format: ReportFormat

    @abstractmethod
    def render(self, report: Report) -> ReportOutput:
        raise NotImplementedError


class TextReportRenderer(ReportRenderer):
    format = ReportFormat.TEXT

    def render(self, report: Report) -> ReportOutput:
        lines = [report.definition.title, ""]
        for key, value in report.payload.items():
            lines.append(f"{key}: {value}")
        content = "\n".join(lines).encode("utf-8")
        return ReportOutput(
            name=report.definition.name,
            format=ReportFormat.TEXT,
            content=content,
            content_type="text/plain",
            metadata={"title": report.definition.title},
        )
