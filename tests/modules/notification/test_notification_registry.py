from modules.notification.channel import InMemoryNotificationChannel
from modules.notification import NotificationChannelRegistry


def test_notification_channel_registry_registers_channel():
    registry = NotificationChannelRegistry()
    channel = InMemoryNotificationChannel()

    registry.register(channel)

    assert registry.exists("memory")
    assert registry.get("memory") == channel
