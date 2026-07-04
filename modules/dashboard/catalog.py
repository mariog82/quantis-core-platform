from modules.dashboard.widget import DashboardWidgetDefinition


class DashboardCatalog:
    def __init__(self):
        self._widgets: dict[str, DashboardWidgetDefinition] = {}

    def register(self, widget: DashboardWidgetDefinition) -> DashboardWidgetDefinition:
        self._widgets[widget.key] = widget
        return widget

    def get(self, key: str) -> DashboardWidgetDefinition:
        return self._widgets[key]

    def exists(self, key: str) -> bool:
        return key in self._widgets

    def list_widgets(self) -> list[DashboardWidgetDefinition]:
        return list(self._widgets.values())
