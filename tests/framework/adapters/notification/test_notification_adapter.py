from framework.adapters.notification import (
    InMemoryNotificationAdapter,
    NotificationRecipient,
    NotificationRequest,
)


def test_in_memory_notification_adapter_sends_notification():
    adapter = InMemoryNotificationAdapter()
    request = NotificationRequest(
        recipients=[NotificationRecipient(address="user@example.com")],
        subject="Hello",
        body="World",
    )

    response = adapter.send(request)

    assert response.delivered is True
    assert response.metadata["recipient_count"] == 1


def test_in_memory_notification_adapter_fails_without_recipients():
    adapter = InMemoryNotificationAdapter()
    request = NotificationRequest(recipients=[], subject="Hello", body="World")

    response = adapter.send(request)

    assert response.delivered is False
    assert response.error == "NO_RECIPIENTS"


def test_notification_adapter_execute_send_and_list_sent():
    adapter = InMemoryNotificationAdapter()

    send_result = adapter.execute(
        "send",
        {
            "request": NotificationRequest(
                recipients=[NotificationRecipient(address="user@example.com")],
                subject="Hello",
                body="World",
            )
        },
    )

    list_result = adapter.execute("list_sent")

    assert send_result.success is True
    assert list_result.success is True
    assert len(list_result.data) == 1
