# Human Tasks Architecture

```text
Human workflow step
      ↓
HumanTaskStepExecutor
      ↓
HumanTaskService
      ↓
HumanTaskRepository
      ↓
HumanTask lifecycle
  claim → start → complete
      ├── release
      └── delegate
```
