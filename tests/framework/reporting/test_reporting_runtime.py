from framework.reporting import ReportContext, ReportDefinition, ReportId, ReportingRuntime


def provider(context: ReportContext) -> dict:
    return {"tenant_id": context.tenant_id, "total": 10}


def test_reporting_runtime_generates_text_report():
    runtime = ReportingRuntime()
    runtime.register(ReportDefinition(id=ReportId(), name="summary", title="Summary Report", provider=provider))
    output = runtime.generate("summary", ReportContext(tenant_id="tenant-demo"))
    assert output.name == "summary"
    assert output.content_type == "text/plain"
    assert b"tenant-demo" in output.content
    assert b"total: 10" in output.content
