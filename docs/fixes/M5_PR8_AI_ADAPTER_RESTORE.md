# M5 PR8 AI Adapter Restore

## Problema

Durante la PR8 il package `framework.adapters.ai` è stato ridotto a marker cumulativo e non esportava più i simboli reali richiesti dai test:

- `AIEmbeddingRequest`
- `AIMessage`
- `AIModel`
- `AIProviderType`
- `AIRequest`
- `AIRole`

## Correzione

Ripristinati i sorgenti reali dell'AI Adapter:

- `framework/adapters/ai/__init__.py`
- `framework/adapters/ai/contracts.py`
- `framework/adapters/ai/adapter.py`
- `framework/adapters/ai/factory.py`
