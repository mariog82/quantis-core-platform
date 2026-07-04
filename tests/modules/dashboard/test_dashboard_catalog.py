from modules.dashboard import DashboardCatalog, DashboardWidgetDefinition


def test_dashboard_catalog_registers_widget():
    catalog = DashboardCatalog()
    widget = DashboardWidgetDefinition(key="demo", title="Demo", provider=lambda data: 1)

    catalog.register(widget)

    assert catalog.exists("demo")
    assert catalog.get("demo") == widget
