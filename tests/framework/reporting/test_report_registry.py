from framework.reporting import ReportDefinition, ReportId, ReportRegistry


def test_register_and_get_report_definition():
    registry = ReportRegistry()
    definition = ReportDefinition(id=ReportId(), name="demo", title="Demo Report")
    registry.register(definition)
    assert registry.exists("demo")
    assert registry.get("demo") == definition


def test_list_reports():
    registry = ReportRegistry()
    registry.register(ReportDefinition(id=ReportId(), name="a", title="A"))
    registry.register(ReportDefinition(id=ReportId(), name="b", title="B"))
    assert len(registry.list_reports()) == 2
