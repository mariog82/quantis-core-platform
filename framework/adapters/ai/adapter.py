from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.ai.contracts import (
    AICompletionChoice,
    AIEmbedding,
    AIEmbeddingRequest,
    AIEmbeddingResponse,
    AIMessage,
    AIRequest,
    AIResponse,
    AIRole,
    AIUsage,
)


class AIAdapter(Adapter):
    metadata = AdapterMetadata(
        name="ai",
        adapter_type="ai",
        version="0.5.0-beta.1",
        capabilities=["ai"],
        provider="quantis",
    )

    def complete(self, request: AIRequest) -> AIResponse:
        raise NotImplementedError

    def embed(self, request: AIEmbeddingRequest) -> AIEmbeddingResponse:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}
        if operation == "complete":
            return AdapterResult.ok(self.complete(payload["request"]))
        if operation == "embed":
            return AdapterResult.ok(self.embed(payload["request"]))
        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryAIAdapter(AIAdapter):
    def complete(self, request: AIRequest) -> AIResponse:
        prompt = next(
            (message.content for message in reversed(request.messages) if message.role == AIRole.USER),
            "",
        )
        content = f"InMemoryAI response: {prompt}".strip()
        return AIResponse(
            choices=[AICompletionChoice(AIMessage(AIRole.ASSISTANT, content))],
            usage=AIUsage(total_tokens=len(content.split())),
        )

    def embed(self, request: AIEmbeddingRequest) -> AIEmbeddingResponse:
        inputs = request.input if isinstance(request.input, list) else [request.input]
        return AIEmbeddingResponse(
            [
                AIEmbedding([float(len(item)), float(index)], index)
                for index, item in enumerate(inputs)
            ]
        )
