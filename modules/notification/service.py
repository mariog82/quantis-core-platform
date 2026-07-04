from modules.notification.channel import InMemoryNotificationChannel, NotificationChannel
from modules.notification.message import NotificationMessage
from modules.notification.registry import NotificationChannelRegistry


class NotificationService:
    def __init__(self, registry: NotificationChannelRegistry | None = None):
        self.registry = registry or NotificationChannelRegistry()
        if not self.registry.exists("memory"):
            self.registry.register(InMemoryNotificationChannel())

    def register_channel(self, channel: NotificationChannel) -> NotificationChannel:
        return self.registry.register(channel)

    def send(self, channel_name: str, message: NotificationMessage) -> bool:
        channel = self.registry.get(channel_name)
        return channel.send(message)

    def send_default(self, message: NotificationMessage) -> bool:
        return self.send("memory", message)
