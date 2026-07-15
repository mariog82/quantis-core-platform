from core.knowledge_graph import GraphNode, InMemoryGraphRepository, KnowledgeGraph

def test_repository_returns_isolated_graph_copies():
    repository = InMemoryGraphRepository()
    graph = KnowledgeGraph()
    graph.add_node(GraphNode("document", {"title": "Original"}))
    repository.save("docs", graph)
    loaded = repository.get("docs")
    assert loaded is not None
    loaded.add_node(GraphNode("document", {"title": "Local"}))
    again = repository.get("docs")
    assert again is not None
    assert again.node_count == 1
