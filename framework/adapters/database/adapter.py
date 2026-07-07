from abc import abstractmethod

from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.database.contracts import (
    DatabaseCommand,
    DatabaseConnectionConfig,
    #DatabaseDialect,
    DatabaseQuery,
    DatabaseRecord,
    DatabaseResult,
)


class DatabaseAdapter(Adapter):
    metadata = AdapterMetadata(
        name="database",
        adapter_type="database",
        version="0.5.0-alpha.3",
        description="Provider-neutral database adapter contract.",
        capabilities=["database", "query", "command"],
        provider="quantis",
    )

    @abstractmethod
    def connect(self, config: DatabaseConnectionConfig) -> None:
        raise NotImplementedError

    @abstractmethod
    def query(self, query: DatabaseQuery) -> DatabaseResult:
        raise NotImplementedError

    @abstractmethod
    def execute_command(self, command: DatabaseCommand) -> DatabaseResult:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}

        if operation == "connect":
            config = payload.get("config")
            if not isinstance(config, DatabaseConnectionConfig):
                return AdapterResult.fail("INVALID_DATABASE_CONFIG")
            self.connect(config)
            return AdapterResult.ok({"connected": True})

        if operation == "query":
            query = payload.get("query")
            if not isinstance(query, DatabaseQuery):
                return AdapterResult.fail("INVALID_DATABASE_QUERY")
            return AdapterResult.ok(self.query(query))

        if operation == "command":
            command = payload.get("command")
            if not isinstance(command, DatabaseCommand):
                return AdapterResult.fail("INVALID_DATABASE_COMMAND")
            return AdapterResult.ok(self.execute_command(command))

        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryDatabaseAdapter(DatabaseAdapter):
    def __init__(self):
        super().__init__()
        self.connected = False
        self.config: DatabaseConnectionConfig | None = None
        self.tables: dict[str, list[dict]] = {}

    def connect(self, config: DatabaseConnectionConfig) -> None:
        self.config = config
        self.connected = True

    def create_table(self, name: str) -> None:
        self.tables.setdefault(name, [])

    def insert(self, table: str, row: dict) -> DatabaseResult:
        self.tables.setdefault(table, []).append(row)
        return DatabaseResult(affected_rows=1)

    def select_all(self, table: str) -> DatabaseResult:
        return DatabaseResult(
            records=[DatabaseRecord(values=row) for row in self.tables.get(table, [])],
            affected_rows=0,
        )

    def query(self, query: DatabaseQuery) -> DatabaseResult:
        table = query.parameters.get("table")
        if query.statement == "select_all" and table:
            return self.select_all(table)
        return DatabaseResult(metadata={"warning": "unsupported_query"})

    def execute_command(self, command: DatabaseCommand) -> DatabaseResult:
        table = command.parameters.get("table")
        if command.statement == "create_table" and table:
            self.create_table(table)
            return DatabaseResult(metadata={"table": table})

        if command.statement == "insert" and table:
            row = command.parameters.get("row", {})
            return self.insert(table, row)

        return DatabaseResult(metadata={"warning": "unsupported_command"})
