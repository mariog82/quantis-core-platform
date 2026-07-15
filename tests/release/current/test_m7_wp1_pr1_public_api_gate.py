import core.knowledge_graph

def test_knowledge_graph_public_api_is_available():
    for symbol in [
        "KnowledgeGraph", "NodeId", "EdgeId", "GraphNode",
        "GraphEdge", "GraphMetadata", "GraphVersion", "JsonGraphSerializer",
    ]:
        assert hasattr(core.knowledge_graph, symbol), symbol
