# Graph Repository Architecture

```text
GraphRepositoryService
        ↓
GraphRepository
        ↓
InMemoryGraphRepository
   ├── save / get / delete
   ├── list_ids
   ├── snapshot
   └── restore
```
