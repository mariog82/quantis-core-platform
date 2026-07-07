from framework.adapters import AdapterContext
from framework.adapters.storage.adapter import InMemoryStorageAdapter


def create_in_memory_storage_adapter(
    context: AdapterContext | None = None,
) -> InMemoryStorageAdapter:
    adapter = InMemoryStorageAdapter()
    if context is not None:
        adapter.configure(context)
    return adapter
