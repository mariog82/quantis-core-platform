from modules.dashboard.catalog import DashboardCatalog
from modules.dashboard.widget import DashboardWidgetDefinition


def create_default_dashboard_catalog() -> DashboardCatalog:
    catalog = DashboardCatalog()

    catalog.register(
        DashboardWidgetDefinition(
            key="total-events",
            title="Total Events",
            provider=lambda data: data.get("total_events", 0),
        )
    )

    catalog.register(
        DashboardWidgetDefinition(
            key="active-users",
            title="Active Users",
            provider=lambda data: data.get("active_users", 0),
        )
    )

    catalog.register(
        DashboardWidgetDefinition(
            key="conversion-rate",
            title="Conversion Rate",
            provider=lambda data: data.get("conversion_rate", 0),
        )
    )

    return catalog
