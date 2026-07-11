# Workflow Engine 2.0 Frozen Architecture

```text
WorkflowDefinition / BPMN
          ↓
WorkflowRegistry
          ↓
WorkflowRuntime
   ├── Step Executors
   ├── State Machine
   ├── Human Tasks
   ├── Timers
   └── Saga Engine
          ↓
Workflow Monitoring
          ↓
Workflow API
          ↓
Python SDK
```

All WP4 public contracts are frozen for release-candidate stabilization.
