from framework.dashboard import (
    Dashboard,
    DashboardContext,
    DashboardId,
    DashboardRuntime,
    DashboardWidget,
    WidgetData,
)


def provider(context: DashboardContext) -> WidgetData:
    return WidgetData(value={"tenant_id": context.tenant_id})


def test_render_dashboard():
    dashboard = Dashboard(id=DashboardId(), name="main", title="Main Dashboard", role="admin")
    dashboard.add_widget(DashboardWidget(key="kpi", title="KPI", provider=provider))

    runtime = DashboardRuntime()
    runtime.register(dashboard)

    result = runtime.render_dashboard("main", DashboardContext(tenant_id="tenant-demo"))

    assert result["name"] == "main"
    assert result["widgets"]["kpi"].value["tenant_id"] == "tenant-demo"


def test_render_single_widget():
    dashboard = Dashboard(id=DashboardId(), name="main", title="Main Dashboard")
    dashboard.add_widget(DashboardWidget(key="summary", title="Summary", provider=provider))

    runtime = DashboardRuntime()
    runtime.register(dashboard)

    widget = runtime.render_widget("main", "summary", DashboardContext(tenant_id="tenant-demo"))

    assert widget.value["tenant_id"] == "tenant-demo"
