# Workflow API and SDK Architecture

```text
WorkflowClient
      ↓
WorkflowTransport
      ↓
WorkflowAPIService
      ├── WorkflowRegistry
      ├── WorkflowRuntime
      └── HumanTaskService

WorkflowAPIService
      ↓
OpenAPI 3.1 contract
```
