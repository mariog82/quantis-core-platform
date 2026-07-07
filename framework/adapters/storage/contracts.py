from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class StorageProviderType(str, Enum):
    FILESYSTEM = "filesystem"
    S3 = "s3"
    AZURE_BLOB = "azure_blob"
    GOOGLE_STORAGE = "google_storage"
    MINIO = "minio"
    MEMORY = "memory"


@dataclass(frozen=True)
class StorageObjectMetadata:
    key: str
    content_type: str = "application/octet-stream"
    size: int = 0
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class StorageObject:
    metadata: StorageObjectMetadata
    content: bytes


@dataclass
class StorageWriteRequest:
    key: str
    content: bytes
    content_type: str = "application/octet-stream"
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class StorageReadRequest:
    key: str
