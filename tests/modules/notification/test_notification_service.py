from modules.notification import NotificationMessage, NotificationService


def test_notification_service_sends_default_message():
    service = NotificationService()
    message = NotificationMessage(
        recipient="user@example.com",
        subject="Hello",
        body="World",
    )

    assert service.send_default(message) is True
    channel = service.registry.get("memory")
    assert channel.messages[0].subject == "Hello"
