from modules.notification.channel import NotificationChannel


class NotificationChannelRegistry:
    def __init__(self):
        self._channels: dict[str, NotificationChannel] = {}

    def register(self, channel: NotificationChannel) -> NotificationChannel:
        self._channels[channel.name] = channel
        return channel

    def get(self, name: str) -> NotificationChannel:
        return self._channels[name]

    def exists(self, name: str) -> bool:
        return name in self._channels

    def list_channels(self) -> list[NotificationChannel]:
        return list(self._channels.values())
