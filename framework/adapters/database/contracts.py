from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class DatabaseDialect(str, Enum):
    SQLITE = "sqlite"
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"
    SQLSERVER = "sqlserver"
    ORACLE = "oracle"
    MEMORY = "memory"


@dataclass
class DatabaseConnectionConfig:
    dialect: DatabaseDialect
    database: str
    host: str | None = None
    port: int | None = None
    username: str | None = None
    password: str | None = None
    options: dict[str, Any] = field(default_factory=dict)


@dataclass
class DatabaseQuery:
    statement: str
    parameters: dict[str, Any] = field(default_factory=dict)


@dataclass
class DatabaseCommand:
    statement: str
    parameters: dict[str, Any] = field(default_factory=dict)


@dataclass
class DatabaseRecord:
    values: dict[str, Any]

    def get(self, key: str, default: Any = None) -> Any:
        return self.values.get(key, default)


@dataclass
class DatabaseResult:
    records: list[DatabaseRecord] = field(default_factory=list)
    affected_rows: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def first(self) -> DatabaseRecord | None:
        return self.records[0] if self.records else None
