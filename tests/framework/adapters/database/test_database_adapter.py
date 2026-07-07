from framework.adapters.database import (
    DatabaseCommand,
    DatabaseConnectionConfig,
    DatabaseDialect,
    DatabaseQuery,
    InMemoryDatabaseAdapter,
)


def test_in_memory_database_adapter_connects():
    adapter = InMemoryDatabaseAdapter()
    adapter.connect(DatabaseConnectionConfig(dialect=DatabaseDialect.MEMORY, database="memory"))

    assert adapter.connected is True


def test_in_memory_database_adapter_insert_and_select():
    adapter = InMemoryDatabaseAdapter()
    adapter.execute_command(DatabaseCommand(statement="create_table", parameters={"table": "items"}))
    adapter.execute_command(
        DatabaseCommand(
            statement="insert",
            parameters={"table": "items", "row": {"id": 1, "name": "demo"}},
        )
    )

    result = adapter.query(DatabaseQuery(statement="select_all", parameters={"table": "items"}))

    assert len(result.records) == 1
    assert result.first.get("name") == "demo"


def test_database_adapter_execute_query_operation():
    adapter = InMemoryDatabaseAdapter()
    adapter.execute("command", {"command": DatabaseCommand("create_table", {"table": "items"})})
    adapter.execute(
        "command",
        {
            "command": DatabaseCommand(
                "insert",
                {"table": "items", "row": {"id": 2}},
            )
        },
    )

    result = adapter.execute(
        "query",
        {"query": DatabaseQuery("select_all", {"table": "items"})},
    )

    assert result.success is True
    assert result.data.first.get("id") == 2
