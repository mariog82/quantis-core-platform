# Query Optimizer Architecture

```text
GraphQuery
    ↓
GraphQueryOptimizer
    ├── RemoveDuplicatePredicates
    ├── ReorderAndPredicates
    └── NormalizePagination
    ↓
GraphQueryPlanner
    ↓
QueryResultCache
    ↓
OptimizedGraphQueryExecutor
```
