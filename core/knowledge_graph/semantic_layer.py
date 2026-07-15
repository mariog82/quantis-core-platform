from core.knowledge_graph.semantic_inference import SemanticInferenceEngine
from core.knowledge_graph.semantic_mapper import SemanticMapper
from core.knowledge_graph.semantic_models import (
    SemanticConcept,
    SemanticMapping,
    SemanticRelationship,
)
from core.knowledge_graph.semantic_registry import SemanticRegistry
from core.knowledge_graph.semantic_validator import (
    SemanticValidationReport,
    SemanticValidator,
)


class SemanticLayerService:
    def __init__(
        self,
        registry: SemanticRegistry | None = None,
        validator: SemanticValidator | None = None,
        inference_engine: SemanticInferenceEngine | None = None,
    ) -> None:
        self.registry = registry or SemanticRegistry()
        self.validator = validator or SemanticValidator()
        self.inference_engine = inference_engine or SemanticInferenceEngine()
        self.mapper = SemanticMapper(self.registry)

    def add_concept(self, concept: SemanticConcept) -> SemanticConcept:
        report = self.validator.validate_concept(concept, self.registry)
        if not report.passed:
            raise ValueError(", ".join(issue.code for issue in report.issues))
        return self.registry.register_concept(concept)

    def add_relationship(
        self,
        relationship: SemanticRelationship,
    ) -> SemanticRelationship:
        report = self.validator.validate_relationship(relationship, self.registry)
        if not report.passed:
            raise ValueError(", ".join(issue.code for issue in report.issues))
        return self.registry.register_relationship(relationship)

    def map_term(self, term: str) -> SemanticMapping | None:
        return self.mapper.map_term(term)

    def validate_concept(
        self,
        concept: SemanticConcept,
    ) -> SemanticValidationReport:
        return self.validator.validate_concept(concept, self.registry)
