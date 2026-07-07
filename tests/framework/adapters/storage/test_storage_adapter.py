from framework.adapters.storage import (
    InMemoryStorageAdapter,
    StorageReadRequest,
    StorageWriteRequest,
)


def test_in_memory_storage_adapter_write_read_exists_delete():
    adapter = InMemoryStorageAdapter()

    metadata = adapter.write(
        StorageWriteRequest(
            key="docs/readme.txt",
            content=b"hello",
            content_type="text/plain",
        )
    )

    assert metadata.size == 5
    assert adapter.exists("docs/readme.txt") is True
    assert adapter.read(StorageReadRequest(key="docs/readme.txt")).content == b"hello"
    assert adapter.delete("docs/readme.txt") is True
    assert adapter.exists("docs/readme.txt") is False


def test_in_memory_storage_adapter_lists_keys_by_prefix():
    adapter = InMemoryStorageAdapter()
    adapter.write(StorageWriteRequest(key="docs/a.txt", content=b"a"))
    adapter.write(StorageWriteRequest(key="docs/b.txt", content=b"b"))
    adapter.write(StorageWriteRequest(key="img/c.png", content=b"c"))

    assert adapter.list_keys("docs/") == ["docs/a.txt", "docs/b.txt"]


def test_storage_adapter_execute_operations():
    adapter = InMemoryStorageAdapter()

    write_result = adapter.execute(
        "write",
        {
            "request": StorageWriteRequest(
                key="file.txt",
                content=b"data",
                content_type="text/plain",
            )
        },
    )

    read_result = adapter.execute(
        "read",
        {"request": StorageReadRequest(key="file.txt")},
    )

    exists_result = adapter.execute("exists", {"key": "file.txt"})

    assert write_result.success is True
    assert read_result.success is True
    assert read_result.data.content == b"data"
    assert exists_result.data["exists"] is True
