from framework.adapters import AdapterContext
from framework.adapters.sdk.adapter import InMemorySDKAdapter

def create_in_memory_sdk_adapter(context: AdapterContext | None = None) -> InMemorySDKAdapter:
    adapter = InMemorySDKAdapter()
    if context is not None:
        adapter.configure(context)
    return adapter
