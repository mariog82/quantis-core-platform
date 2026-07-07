from framework.adapters.database import (
    DatabaseConnectionConfig,
    DatabaseDialect,
    DatabaseRecord,
    DatabaseResult,
)


def test_database_connection_config():
    config = DatabaseConnectionConfig(
        dialect=DatabaseDialect.POSTGRESQL,
        database="quantis",
        host="localhost",
        port=5432,
    )

    assert config.dialect == DatabaseDialect.POSTGRESQL
    assert config.database == "quantis"


def test_database_record_and_result():
    record = DatabaseRecord(values={"id": 1, "name": "demo"})
    result = DatabaseResult(records=[record])

    assert result.first.get("name") == "demo"
