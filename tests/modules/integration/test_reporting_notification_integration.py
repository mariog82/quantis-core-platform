from modules.notification import NotificationModule
from modules.reporting import ReportingModule


def test_reporting_output_can_be_notified():
    reporting = ReportingModule()
    notification = NotificationModule()

    content = reporting.generate(
        "summary",
        {
            "total_events": 12,
            "active_users": 3,
            "conversion_rate": 0.25,
        },
    )

    sent = notification.send(
        recipient="admin@example.com",
        subject="Report generated",
        body=content.decode("utf-8"),
    )

    assert sent is True
    channel = notification.service.registry.get("memory")
    assert channel.messages[0].recipient == "admin@example.com"
    assert "Summary Report" in channel.messages[0].body
