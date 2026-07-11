# Workflow Core Architecture

```text
WorkflowDefinition
  ├── WorkflowStepDefinition[]
  └── WorkflowTransition[]

WorkflowInstance
  ├── WorkflowId
  ├── WorkflowVersion
  ├── WorkflowInstanceId
  ├── WorkflowContext
  └── WorkflowState
```
