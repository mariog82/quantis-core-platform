from abc import abstractmethod

from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.ai.contracts import (
    AICompletionChoice,
    AIEmbedding,
    AIEmbeddingRequest,
    AIEmbeddingResponse,
    AIMessage,
    AIProviderType,
    AIRequest,
    AIResponse,
    AIRole,
    AIUsage,
)


class AIAdapter(Adapter):
    metadata = AdapterMetadata(
        name="ai",
        adapter_type="ai",
        version="0.5.0-alpha.8",
        description="Provider-neutral AI adapter contract.",
        capabilities=["ai", "completion", "embedding"],
        provider="quantis",
    )

    @abstractmethod
    def complete(self, request: AIRequest) -> AIResponse:
        raise NotImplementedError

    @abstractmethod
    def embed(self, request: AIEmbeddingRequest) -> AIEmbeddingResponse:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}

        if operation == "complete":
            request = payload.get("request")
            if not isinstance(request, AIRequest):
                return AdapterResult.fail("INVALID_AI_REQUEST")
            return AdapterResult.ok(self.complete(request))

        if operation == "embed":
            request = payload.get("request")
            if not isinstance(request, AIEmbeddingRequest):
                return AdapterResult.fail("INVALID_AI_EMBEDDING_REQUEST")
            return AdapterResult.ok(self.embed(request))

        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryAIAdapter(AIAdapter):
    metadata = AdapterMetadata(
        name="memory-ai",
        adapter_type="ai",
        version="0.5.0-alpha.8",
        description="In-memory AI adapter for tests.",
        capabilities=["ai", "completion", "embedding"],
        provider=AIProviderType.MEMORY.value,
    )

    def complete(self, request: AIRequest) -> AIResponse:
        user_messages = [
            message.content
            for message in request.messages
            if message.role == AIRole.USER
        ]
        prompt = user_messages[-1] if user_messages else ""
        content = f"InMemoryAI response: {prompt}".strip()

        prompt_tokens = sum(len(message.content.split()) for message in request.messages)
        completion_tokens = len(content.split())

        return AIResponse(
            choices=[
                AICompletionChoice(
                    message=AIMessage(role=AIRole.ASSISTANT, content=content)
                )
            ],
            usage=AIUsage(
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens,
                total_tokens=prompt_tokens + completion_tokens,
            ),
        )

    def embed(self, request: AIEmbeddingRequest) -> AIEmbeddingResponse:
        inputs = request.input if isinstance(request.input, list) else [request.input]
        embeddings = []

        for index, item in enumerate(inputs):
            values = [
                float(len(item)),
                float(sum(ord(char) for char in item) % 997),
                float(index),
            ]
            embeddings.append(AIEmbedding(values=values, index=index))

        return AIEmbeddingResponse(
            embeddings=embeddings,
            usage=AIUsage(prompt_tokens=sum(len(item.split()) for item in inputs)),
        )
