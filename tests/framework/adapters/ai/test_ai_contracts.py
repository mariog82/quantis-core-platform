from framework.adapters.ai import AIMessage, AIModel, AIProviderType, AIRequest, AIRole

def test_ai_request_contract():
    model = AIModel(name="memory-model", provider=AIProviderType.MEMORY)
    request = AIRequest(model=model, messages=[AIMessage(role=AIRole.USER, content="hello")])
    assert request.model.name == "memory-model"
    assert request.messages[0].content == "hello"
