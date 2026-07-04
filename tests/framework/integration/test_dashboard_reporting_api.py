from framework.api import BaseController, RequestContext
from framework.dashboard import (
    Dashboard,
    DashboardContext,
    DashboardId,
    DashboardRuntime,
    DashboardWidget,
    WidgetData,
)
from framework.reporting import ReportContext, ReportDefinition, ReportId, ReportingRuntime


def widget_provider(context: DashboardContext) -> WidgetData:
    return WidgetData(value={"tenant_id": context.tenant_id, "total": 10})


def report_provider(context: ReportContext) -> dict:
    return {"tenant_id": context.tenant_id, "total": 10}


def test_dashboard_reporting_api_integration():
    dashboard = Dashboard(id=DashboardId(), name="main", title="Main Dashboard", role="admin")
    dashboard.add_widget(DashboardWidget(key="summary", title="Summary", provider=widget_provider))

    dashboard_runtime = DashboardRuntime()
    dashboard_runtime.register(dashboard)
    rendered = dashboard_runtime.render_dashboard("main", DashboardContext(tenant_id="tenant-demo"))

    reporting_runtime = ReportingRuntime()
    reporting_runtime.register(
        ReportDefinition(
            id=ReportId(),
            name="summary-report",
            title="Summary Report",
            provider=report_provider,
        )
    )
    output = reporting_runtime.generate("summary-report", ReportContext(tenant_id="tenant-demo"))

    controller = BaseController(RequestContext(tenant_id="tenant-demo"))
    result = controller.ok({"dashboard": rendered["name"], "report": output.name})

    assert result.success is True
    assert result.data["dashboard"] == "main"
    assert result.data["report"] == "summary-report"
    assert b"tenant-demo" in output.content
