from framework.adapters import AdapterContext
from framework.adapters.database.adapter import InMemoryDatabaseAdapter
from framework.adapters.database.contracts import DatabaseConnectionConfig, DatabaseDialect


def create_in_memory_database_adapter(
    context: AdapterContext | None = None,
) -> InMemoryDatabaseAdapter:
    adapter = InMemoryDatabaseAdapter()
    if context is not None:
        adapter.configure(context)
    adapter.connect(
        DatabaseConnectionConfig(
            dialect=DatabaseDialect.MEMORY,
            database="memory",
        )
    )
    return adapter
