from framework.dashboard.exceptions import WidgetNotFound
from framework.dashboard.models import Dashboard, DashboardContext, WidgetData
from framework.dashboard.registry import DashboardRegistry


class DashboardRuntime:
    def __init__(self, registry: DashboardRegistry | None = None):
        self.registry = registry or DashboardRegistry()

    def register(self, dashboard: Dashboard) -> Dashboard:
        return self.registry.register(dashboard)

    def render_dashboard(self, name: str, context: DashboardContext | None = None) -> dict:
        dashboard = self.registry.get(name)
        context = context or DashboardContext(role=dashboard.role)

        widgets = {}
        for widget_key in dashboard.layout.widgets:
            widget = dashboard.widgets.get(widget_key)
            if widget is None:
                raise WidgetNotFound(widget_key)
            widgets[widget_key] = widget.render(context)

        return {
            "name": dashboard.name,
            "title": dashboard.title,
            "role": dashboard.role,
            "layout": dashboard.layout,
            "widgets": widgets,
        }

    def render_widget(
        self,
        dashboard_name: str,
        widget_key: str,
        context: DashboardContext | None = None,
    ) -> WidgetData:
        dashboard = self.registry.get(dashboard_name)
        widget = dashboard.widgets.get(widget_key)
        if widget is None:
            raise WidgetNotFound(widget_key)
        return widget.render(context or DashboardContext(role=dashboard.role))
