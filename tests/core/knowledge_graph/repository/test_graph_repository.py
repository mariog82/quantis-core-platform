from core.knowledge_graph import GraphNode, InMemoryGraphRepository, KnowledgeGraph

def test_repository_saves_and_loads_graph():
    repository = InMemoryGraphRepository()
    graph = KnowledgeGraph()
    graph.add_node(GraphNode("document", {"title": "Delibera"}))
    repository.save("governance", graph)
    restored = repository.get("governance")
    assert restored is not None
    assert restored.node_count == 1
    assert repository.list_ids() == ["governance"]
