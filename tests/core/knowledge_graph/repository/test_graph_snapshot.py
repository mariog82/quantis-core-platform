from core.knowledge_graph import GraphNode, InMemoryGraphRepository, KnowledgeGraph

def test_repository_snapshot_and_restore():
    repository = InMemoryGraphRepository()
    graph = KnowledgeGraph()
    node = graph.add_node(GraphNode("person", {"name": "Mario"}))
    repository.save("people", graph)
    snapshot = repository.snapshot("people")
    repository.delete("people")
    restored = repository.restore(snapshot)
    assert snapshot.revision == 1
    assert restored.get_node(node.node_id).properties["name"] == "Mario"
