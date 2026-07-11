from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class AIProviderType(str, Enum):
    MEMORY = "memory"
    OPENAI = "openai"
    ANTHROPIC = "anthropic"


class AIRole(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


@dataclass(frozen=True)
class AIModel:
    name: str
    provider: AIProviderType = AIProviderType.MEMORY


@dataclass
class AIMessage:
    role: AIRole
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class AIRequest:
    model: AIModel
    messages: list[AIMessage]
    temperature: float = 0.0


@dataclass
class AICompletionChoice:
    message: AIMessage
    finish_reason: str = "stop"


@dataclass
class AIUsage:
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


@dataclass
class AIResponse:
    choices: list[AICompletionChoice]
    usage: AIUsage = field(default_factory=AIUsage)

    @property
    def text(self) -> str:
        return self.choices[0].message.content if self.choices else ""


@dataclass
class AIEmbeddingRequest:
    model: AIModel
    input: str | list[str]


@dataclass
class AIEmbedding:
    values: list[float]
    index: int = 0


@dataclass
class AIEmbeddingResponse:
    embeddings: list[AIEmbedding]
    usage: AIUsage = field(default_factory=AIUsage)
