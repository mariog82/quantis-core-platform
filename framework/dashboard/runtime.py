from framework.dashboard.models import Dashboard, DashboardContext, WidgetData


class DashboardRuntime:
    def __init__(self):
        self._dashboards: dict[str, Dashboard] = {}

    def register(self, dashboard: Dashboard) -> Dashboard:
        self._dashboards[dashboard.name] = dashboard
        return dashboard

    def render_dashboard(self, name: str, context: DashboardContext | None = None) -> dict:
        dashboard = self._dashboards[name]
        ctx = context or DashboardContext()
        return {
            "name": dashboard.name,
            "widgets": {key: dashboard.widgets[key].render(ctx) for key in dashboard.layout.widgets},
        }

    def render_widget(self, dashboard_name: str, widget_key: str, context: DashboardContext | None = None) -> WidgetData:
        return self._dashboards[dashboard_name].widgets[widget_key].render(context or DashboardContext())
