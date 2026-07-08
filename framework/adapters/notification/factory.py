from framework.adapters.notification.adapter import InMemoryNotificationAdapter

def create_in_memory_notification_adapter(context=None):
    adapter = InMemoryNotificationAdapter()
    if context is not None:
        adapter.configure(context)
    return adapter
