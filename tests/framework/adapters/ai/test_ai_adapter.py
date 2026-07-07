from framework.adapters.ai import AIEmbeddingRequest, AIMessage, AIModel, AIProviderType, AIRequest, AIRole, InMemoryAIAdapter

def test_in_memory_ai_adapter_completes_request():
    adapter = InMemoryAIAdapter()
    request = AIRequest(
        model=AIModel(name="memory-model", provider=AIProviderType.MEMORY),
        messages=[AIMessage(role=AIRole.USER, content="Explain Quantis")],
    )
    response = adapter.complete(request)
    assert "Explain Quantis" in response.text
    assert response.usage.total_tokens > 0

def test_in_memory_ai_adapter_generates_embeddings():
    adapter = InMemoryAIAdapter()
    request = AIEmbeddingRequest(
        model=AIModel(name="memory-embedding", provider=AIProviderType.MEMORY),
        input=["alpha", "beta"],
    )
    response = adapter.embed(request)
    assert len(response.embeddings) == 2
    assert response.embeddings[0].index == 0

def test_ai_adapter_execute_complete_and_embed():
    adapter = InMemoryAIAdapter()
    model = AIModel(name="memory-model", provider=AIProviderType.MEMORY)
    complete_result = adapter.execute(
        "complete",
        {"request": AIRequest(model=model, messages=[AIMessage(role=AIRole.USER, content="hello")])},
    )
    embed_result = adapter.execute("embed", {"request": AIEmbeddingRequest(model=model, input="hello")})
    assert complete_result.success is True
    assert embed_result.success is True
    assert len(embed_result.data.embeddings) == 1
