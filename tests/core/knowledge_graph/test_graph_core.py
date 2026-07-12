import pytest
from core.knowledge_graph import GraphEdge, GraphMetadata, GraphNode, JsonGraphSerializer, KnowledgeGraph, NodeNotFound

def test_graph_core_roundtrip():
    graph = KnowledgeGraph()
    document = graph.add_node(GraphNode(
        node_type="document",
        properties={"title": "Delibera"},
        metadata=GraphMetadata(tenant_id="school-1", source="deliberascuola"),
    ))
    regulation = graph.add_node(GraphNode(
        node_type="regulation",
        properties={"code": "GDPR"},
    ))
    graph.add_edge(GraphEdge(
        source_id=document.node_id,
        target_id=regulation.node_id,
        relation_type="references",
        weight=0.9,
    ))
    restored = JsonGraphSerializer().deserialize(JsonGraphSerializer().serialize(graph))
    assert restored.node_count == 2
    assert restored.edge_count == 1
    assert restored.neighbors(document.node_id)[0].node_type == "regulation"

def test_graph_updates_version_and_rejects_unknown_target():
    graph = KnowledgeGraph()
    source = graph.add_node(GraphNode(node_type="person", properties={"name": "Mario"}))
    updated = graph.update_node(source.node_id, properties={"name": "Mario", "role": "founder"})
    assert updated.version.value == 2

    unknown = GraphNode(node_type="organization", properties={})
    with pytest.raises(NodeNotFound):
        graph.add_edge(GraphEdge(
            source_id=source.node_id,
            target_id=unknown.node_id,
            relation_type="founded",
        ))
