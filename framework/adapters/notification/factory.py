from framework.adapters import AdapterContext
from framework.adapters.notification.adapter import InMemoryNotificationAdapter


def create_in_memory_notification_adapter(
    context: AdapterContext | None = None,
) -> InMemoryNotificationAdapter:
    adapter = InMemoryNotificationAdapter()
    if context is not None:
        adapter.configure(context)
    return adapter
