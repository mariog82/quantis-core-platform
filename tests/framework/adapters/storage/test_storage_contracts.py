from framework.adapters.storage import StorageObjectMetadata, StorageWriteRequest


def test_storage_write_request_and_metadata():
    request = StorageWriteRequest(
        key="docs/readme.txt",
        content=b"hello",
        content_type="text/plain",
        tags={"area": "docs"},
    )

    metadata = StorageObjectMetadata(
        key=request.key,
        content_type=request.content_type,
        size=len(request.content),
        tags=request.tags,
    )

    assert metadata.key == "docs/readme.txt"
    assert metadata.size == 5
    assert metadata.tags["area"] == "docs"
