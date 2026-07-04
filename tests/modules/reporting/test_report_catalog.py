from modules.reporting import ReportCatalog, ReportTemplate


def test_report_catalog_registers_template():
    catalog = ReportCatalog()
    template = ReportTemplate(key="demo", title="Demo", fields=["a"])

    catalog.register(template)

    assert catalog.exists("demo")
    assert catalog.get("demo") == template
