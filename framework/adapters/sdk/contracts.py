from dataclasses import dataclass, field
from enum import Enum
from typing import Any

class SDKProviderType(str, Enum):
    MEMORY = "memory"
    PYTHON = "python"
    TYPESCRIPT = "typescript"
    JAVA = "java"
    CSHARP = "csharp"
    GO = "go"

class SDKLanguage(str, Enum):
    PYTHON = "python"
    TYPESCRIPT = "typescript"
    JAVA = "java"
    CSHARP = "csharp"
    GO = "go"

@dataclass(frozen=True)
class SDKCallRequest:
    operation: str
    payload: dict[str, Any] = field(default_factory=dict)
    language: SDKLanguage = SDKLanguage.PYTHON

@dataclass
class SDKCallResponse:
    success: bool
    data: Any = None
    error: str | None = None
