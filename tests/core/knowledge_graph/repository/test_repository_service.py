import pytest
from core.knowledge_graph import GraphRepositoryService, InMemoryGraphRepository

def test_repository_service_prevents_duplicate_creation():
    service = GraphRepositoryService(InMemoryGraphRepository())
    service.create("main")
    with pytest.raises(ValueError, match="Graph already exists"):
        service.create("main")
