from framework.reporting import Report, ReportContext, ReportDefinition, ReportFormat, ReportId, TextReportRenderer


def test_text_report_renderer():
    definition = ReportDefinition(id=ReportId(), name="demo", title="Demo")
    report = Report(definition=definition, payload={"value": 1}, context=ReportContext())
    output = TextReportRenderer().render(report)
    assert output.format == ReportFormat.TEXT
    assert b"value: 1" in output.content
