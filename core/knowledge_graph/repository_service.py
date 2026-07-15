from core.knowledge_graph.graph import KnowledgeGraph
from core.knowledge_graph.repository import GraphRepository, GraphSnapshot

class GraphRepositoryService:
    def __init__(self, repository: GraphRepository) -> None:
        self.repository = repository

    def create(self, graph_id: str, graph: KnowledgeGraph | None = None) -> KnowledgeGraph:
        if self.repository.exists(graph_id):
            raise ValueError(f"Graph already exists: {graph_id}")
        return self.repository.save(graph_id, graph or KnowledgeGraph())

    def load(self, graph_id: str) -> KnowledgeGraph:
        graph = self.repository.get(graph_id)
        if graph is None:
            raise KeyError(graph_id)
        return graph

    def persist(self, graph_id: str, graph: KnowledgeGraph) -> KnowledgeGraph:
        return self.repository.save(graph_id, graph)

    def delete(self, graph_id: str) -> KnowledgeGraph:
        return self.repository.delete(graph_id)

    def snapshot(self, graph_id: str) -> GraphSnapshot:
        return self.repository.snapshot(graph_id)

    def restore(self, snapshot: GraphSnapshot) -> KnowledgeGraph:
        return self.repository.restore(snapshot)
