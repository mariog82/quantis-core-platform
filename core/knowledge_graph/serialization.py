import json
from datetime import datetime
from typing import Protocol
from core.knowledge_graph.graph import KnowledgeGraph
from core.knowledge_graph.identifiers import EdgeId, NodeId
from core.knowledge_graph.models import GraphEdge, GraphMetadata, GraphNode, GraphVersion

class GraphSerializer(Protocol):
    def serialize(self, graph: KnowledgeGraph) -> str:
        ...

class GraphDeserializer(Protocol):
    def deserialize(self, payload: str) -> KnowledgeGraph:
        ...

class JsonGraphSerializer:
    def serialize(self, graph: KnowledgeGraph) -> str:
        data = {
            "nodes": [{
                "node_id": node.node_id.value,
                "node_type": node.node_type,
                "properties": node.properties,
                "metadata": self._metadata_to_dict(node.metadata),
                "version": node.version.value,
            } for node in graph.nodes()],
            "edges": [{
                "edge_id": edge.edge_id.value,
                "source_id": edge.source_id.value,
                "target_id": edge.target_id.value,
                "relation_type": edge.relation_type,
                "properties": edge.properties,
                "directed": edge.directed,
                "weight": edge.weight,
                "metadata": self._metadata_to_dict(edge.metadata),
                "version": edge.version.value,
            } for edge in graph.edges()],
        }
        return json.dumps(data, sort_keys=True)

    def deserialize(self, payload: str) -> KnowledgeGraph:
        data = json.loads(payload)
        graph = KnowledgeGraph()
        for item in data.get("nodes", []):
            graph.add_node(GraphNode(
                node_id=NodeId(item["node_id"]),
                node_type=item["node_type"],
                properties=dict(item.get("properties", {})),
                metadata=self._metadata_from_dict(item.get("metadata", {})),
                version=GraphVersion(item.get("version", 1)),
            ))
        for item in data.get("edges", []):
            graph.add_edge(GraphEdge(
                edge_id=EdgeId(item["edge_id"]),
                source_id=NodeId(item["source_id"]),
                target_id=NodeId(item["target_id"]),
                relation_type=item["relation_type"],
                properties=dict(item.get("properties", {})),
                directed=bool(item.get("directed", True)),
                weight=float(item.get("weight", 1.0)),
                metadata=self._metadata_from_dict(item.get("metadata", {})),
                version=GraphVersion(item.get("version", 1)),
            ))
        return graph

    @staticmethod
    def _metadata_to_dict(metadata: GraphMetadata) -> dict:
        return {
            "tenant_id": metadata.tenant_id,
            "source": metadata.source,
            "correlation_id": metadata.correlation_id,
            "created_by": metadata.created_by,
            "labels": list(metadata.labels),
            "attributes": metadata.attributes,
            "created_at": metadata.created_at.isoformat(),
            "updated_at": metadata.updated_at.isoformat(),
        }

    @staticmethod
    def _metadata_from_dict(data: dict) -> GraphMetadata:
        return GraphMetadata(
            tenant_id=data.get("tenant_id"),
            source=data.get("source"),
            correlation_id=data.get("correlation_id"),
            created_by=data.get("created_by"),
            labels=tuple(data.get("labels", ())),
            attributes=dict(data.get("attributes", {})),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else GraphMetadata().created_at,
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else GraphMetadata().updated_at,
        )
