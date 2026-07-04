from modules.dashboard import DashboardModule, DashboardModuleService, DashboardWidgetDefinition


def test_dashboard_module_builds_default_dashboard():
    module = DashboardModule()
    module.initialize(context={})
    module.start()

    result = module.build_dashboard(
        "main",
        "Main Dashboard",
        {
            "total_events": 100,
            "active_users": 25,
            "conversion_rate": 0.25,
        },
    )

    assert result["name"] == "main"
    assert "total-events" in result["widgets"]
    assert result["widgets"]["total-events"].value == 100


def test_dashboard_module_service_registers_widget():
    service = DashboardModuleService()
    service.register_widget(
        DashboardWidgetDefinition(
            key="custom",
            title="Custom",
            provider=lambda data: data["value"],
        )
    )

    result = service.build_dashboard("custom-dashboard", "Custom", {"value": 7})

    assert result["widgets"]["custom"].value == 7
