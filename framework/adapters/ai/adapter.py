from abc import abstractmethod
from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.ai.contracts import (
    AICompletionChoice, AIEmbedding, AIEmbeddingRequest, AIEmbeddingResponse,
    AIMessage, AIProviderType, AIRequest, AIResponse, AIRole, AIUsage,
)

class AIAdapter(Adapter):
    metadata = AdapterMetadata(
        name="ai",
        adapter_type="ai",
        version="0.5.0-alpha.7",
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
        version="0.5.0-alpha.7",
        description="In-memory AI adapter for tests.",
        capabilities=["ai", "completion", "embedding"],
        provider=AIProviderType.MEMORY.value,
    )

    def complete(self, request: AIRequest) -> AIResponse:
        user_messages = [m.content for m in request.messages if m.role == AIRole.USER]
        prompt = user_messages[-1] if user_messages else ""
        content = f"InMemoryAI response: {prompt}".strip()
        prompt_tokens = sum(len(m.content.split()) for m in request.messages)
        completion_tokens = len(content.split())
        return AIResponse(
            choices=[AICompletionChoice(message=AIMessage(role=AIRole.ASSISTANT, content=content))],
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
            embeddings.append(AIEmbedding(
                values=[float(len(item)), float(sum(ord(c) for c in item) % 997), float(index)],
                index=index,
            ))
        return AIEmbeddingResponse(
            embeddings=embeddings,
            usage=AIUsage(prompt_tokens=sum(len(i.split()) for i in inputs)),
        )
