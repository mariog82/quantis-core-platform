# Knowledge Graph Core Architecture

```text
KnowledgeGraph
  ├── GraphNode[]
  │    ├── NodeId
  │    ├── properties
  │    ├── GraphMetadata
  │    └── GraphVersion
  └── GraphEdge[]
       ├── EdgeId
       ├── source / target
       ├── relation_type
       ├── directed / weight
       ├── GraphMetadata
       └── GraphVersion
```
