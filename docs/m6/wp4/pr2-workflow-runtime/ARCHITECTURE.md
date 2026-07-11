# Workflow Runtime Architecture

```text
WorkflowDefinition
      ↓
WorkflowRuntime.create_instance()
      ↓
WorkflowInstance
      ↓
StepExecutor
      ↓
StepResult
      ├── next step
      ├── waiting
      ├── completed
      └── failed
```
