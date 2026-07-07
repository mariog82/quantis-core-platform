from framework.adapters import AdapterContext
from framework.adapters.messaging.adapter import InMemoryMessagingAdapter

def create_in_memory_messaging_adapter(context: AdapterContext | None = None) -> InMemoryMessagingAdapter:
    adapter = InMemoryMessagingAdapter()
    if context is not None:
        adapter.configure(context)
    return adapter
