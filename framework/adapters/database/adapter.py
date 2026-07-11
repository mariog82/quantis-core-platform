from abc import abstractmethod

from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.database.contracts import DatabaseCommand, DatabaseConnectionConfig, DatabaseQuery, DatabaseRecord, DatabaseResult


class DatabaseAdapter(Adapter):
    metadata = AdapterMetadata(name="database", adapter_type="database", version="0.5.0-beta.1", capabilities=["database"], provider="quantis")

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
        if operation == "query":
            return AdapterResult.ok(self.query(payload["query"]))
        if operation == "command":
            return AdapterResult.ok(self.execute_command(payload["command"]))
        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryDatabaseAdapter(DatabaseAdapter):
    def __init__(self):
        super().__init__()
        self.connected = False
        self.tables: dict[str, list[dict]] = {}

    def connect(self, config: DatabaseConnectionConfig) -> None:
        self.connected = True

    def query(self, query: DatabaseQuery) -> DatabaseResult:
        table = query.parameters.get("table")
        if query.statement == "select_all" and table:
            return DatabaseResult(records=[DatabaseRecord(row) for row in self.tables.get(table, [])])
        return DatabaseResult()

    def execute_command(self, command: DatabaseCommand) -> DatabaseResult:
        table = command.parameters.get("table")
        if command.statement == "create_table" and table:
            self.tables.setdefault(table, [])
            return DatabaseResult()
        if command.statement == "insert" and table:
            self.tables.setdefault(table, []).append(command.parameters.get("row", {}))
            return DatabaseResult(affected_rows=1)
        return DatabaseResult()
