from framework.adapters import AdapterContext
from framework.adapters.database.adapter import InMemoryDatabaseAdapter


def create_in_memory_database_adapter(context: AdapterContext | None = None) -> InMemoryDatabaseAdapter:
    adapter = InMemoryDatabaseAdapter()
    if context is not None:
        adapter.configure(context)
    return adapter
