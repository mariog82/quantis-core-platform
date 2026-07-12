from dataclasses import dataclass
from uuid import uuid4

@dataclass(frozen=True, order=True)
class NodeId:
    value: str

    @classmethod
    def generate(cls) -> "NodeId":
        return cls(str(uuid4()))

    def __str__(self) -> str:
        return self.value

@dataclass(frozen=True, order=True)
class EdgeId:
    value: str

    @classmethod
    def generate(cls) -> "EdgeId":
        return cls(str(uuid4()))

    def __str__(self) -> str:
        return self.value
