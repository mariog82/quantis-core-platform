from framework.adapters.notification import (
    InMemoryNotificationAdapter,
    NotificationRecipient,
    NotificationRequest,
)
from framework.adapters.notification.runtime import NotificationRuntime


def test_notification_runtime_sends_using_adapter():
    runtime = NotificationRuntime(InMemoryNotificationAdapter())

    response = runtime.send(
        NotificationRequest(
            recipients=[NotificationRecipient(address="user@example.com")],
            subject="Hello",
            body="World",
        )
    )

    assert response.delivered is True
    assert len(runtime.list_sent()) == 1
