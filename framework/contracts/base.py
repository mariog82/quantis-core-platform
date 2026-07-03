from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Protocol
from uuid import uuid4


@dataclass(frozen=True)
class ContractId:
    value: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class ContractMetadata:
    name: str
    version: str = "0.1.0"
    description: str = ""
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class FrameworkContract(Protocol):
    metadata: ContractMetadata