from framework.adapters.sdk.adapter import InMemorySDKAdapter

def create_in_memory_sdk_adapter(context=None):
    adapter = InMemorySDKAdapter()
    if context is not None:
        adapter.configure(context)
    return adapter
