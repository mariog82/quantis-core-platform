from framework.dashboard import Dashboard, DashboardContext, DashboardId, DashboardRuntime, DashboardWidget, WidgetData
from modules.dashboard.catalog import DashboardCatalog
from modules.dashboard.widget import DashboardWidgetDefinition


class DashboardModuleService:
    def __init__(
        self,
        catalog: DashboardCatalog | None = None,
        runtime: DashboardRuntime | None = None,
    ):
        self.catalog = catalog or DashboardCatalog()
        self.runtime = runtime or DashboardRuntime()

    def register_widget(self, widget: DashboardWidgetDefinition) -> DashboardWidgetDefinition:
        self.catalog.register(widget)
        return widget

    def build_dashboard(self, name: str, title: str, data: dict) -> dict:
        dashboard = Dashboard(id=DashboardId(), name=name, title=title)

        for widget_definition in self.catalog.list_widgets():
            dashboard.add_widget(
                DashboardWidget(
                    key=widget_definition.key,
                    title=widget_definition.title,
                    provider=lambda context, definition=widget_definition: WidgetData(
                        value=definition.resolve(data)
                    ),
                )
            )

        self.runtime.register(dashboard)
        return self.runtime.render_dashboard(name, DashboardContext())
