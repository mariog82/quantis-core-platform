from modules.reporting import ReportingModule, ReportingModuleService, ReportTemplate


def test_reporting_module_generates_default_summary():
    module = ReportingModule()
    module.initialize(context={})
    module.start()

    content = module.generate(
        "summary",
        {
            "total_events": 100,
            "active_users": 25,
            "conversion_rate": 0.25,
        },
    )

    assert b"Summary Report" in content
    assert b"total_events: 100" in content


def test_reporting_module_service_registers_template():
    service = ReportingModuleService()
    service.register_template(ReportTemplate(key="custom", title="Custom", fields=["value"]))

    content = service.generate("custom", {"value": 7})

    assert b"value: 7" in content
