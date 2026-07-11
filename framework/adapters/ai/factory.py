from framework.adapters import AdapterContext
from framework.adapters.ai.adapter import InMemoryAIAdapter


def create_in_memory_ai_adapter(context: AdapterContext | None = None) -> InMemoryAIAdapter:
    adapter = InMemoryAIAdapter()
    if context is not None:
        adapter.configure(context)
    return adapter
