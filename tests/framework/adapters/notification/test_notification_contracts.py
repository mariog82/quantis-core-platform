from framework.adapters.notification import (
    NotificationChannel,
    NotificationRecipient,
    NotificationRequest,
    NotificationResponse,
    NotificationStatus,
)


def test_notification_request_defaults():
    recipient = NotificationRecipient(address="user@example.com")
    request = NotificationRequest(
        recipients=[recipient],
        subject="Hello",
        body="World",
    )

    assert request.channel == NotificationChannel.EMAIL
    assert request.recipients[0].address == "user@example.com"


def test_notification_response_delivered_property():
    response = NotificationResponse(status=NotificationStatus.SENT)

    assert response.delivered is True
