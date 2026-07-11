# Saga Engine Architecture

```text
SagaDefinition
      ↓
SagaEngine.start()
      ↓
SagaInstance RUNNING
      ↓
Action execution
      ├── success → next step
      └── failure → COMPENSATING
                         ↓
                 reverse compensation
                         ↓
                    COMPENSATED
```
