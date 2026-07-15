# RFC-034 — M7 Query Optimizer

## Goals

- remove duplicate predicates;
- reorder predicates by estimated cost;
- normalize pagination;
- expose optimization reports;
- cache query results;
- track cache hits and misses;
- preserve compatibility with GraphQueryPlanner.
