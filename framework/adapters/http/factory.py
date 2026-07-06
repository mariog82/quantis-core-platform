from framework.adapters import AdapterContext
from framework.adapters.http.client import InMemoryHttpAdapter


def create_in_memory_http_adapter(context: AdapterContext | None = None) -> InMemoryHttpAdapter:
    adapter = InMemoryHttpAdapter()
    if context is not None:
        adapter.configure(context)
    return adapter
