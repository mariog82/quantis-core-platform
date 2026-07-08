from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class StorageProviderType(str, Enum):
    MEMORY = "memory"
    FILESYSTEM = "filesystem"
    S3 = "s3"


@dataclass(frozen=True)
class StorageObjectMetadata:
    key: str
    content_type: str = "application/octet-stream"
    size: int = 0
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
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class StorageReadRequest:
    key: str
