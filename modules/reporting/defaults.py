from modules.reporting.catalog import ReportCatalog
from modules.reporting.template import ReportTemplate


def create_default_report_catalog() -> ReportCatalog:
    catalog = ReportCatalog()
    catalog.register(
        ReportTemplate(
            key="summary",
            title="Summary Report",
            fields=["total_events", "active_users", "conversion_rate"],
        )
    )
    return catalog
