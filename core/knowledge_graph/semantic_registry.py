from core.knowledge_graph.semantic_models import (
    SemanticConcept,
    SemanticMapping,
    SemanticProperty,
    SemanticRelationship,
)


class SemanticRegistry:
    def __init__(self) -> None:
        self._concepts: dict[str, SemanticConcept] = {}
        self._properties: dict[str, SemanticProperty] = {}
        self._relationships: dict[str, SemanticRelationship] = {}
        self._mappings: dict[str, SemanticMapping] = {}

    def register_concept(self, concept: SemanticConcept) -> SemanticConcept:
        if concept.concept_id in self._concepts:
            raise ValueError(f"Concept already registered: {concept.concept_id}")
        self._concepts[concept.concept_id] = concept
        return concept

    def register_property(self, semantic_property: SemanticProperty) -> SemanticProperty:
        if semantic_property.property_id in self._properties:
            raise ValueError(
                f"Property already registered: {semantic_property.property_id}"
            )
        self._properties[semantic_property.property_id] = semantic_property
        return semantic_property

    def register_relationship(self, relationship: SemanticRelationship) -> SemanticRelationship:
        if relationship.relationship_id in self._relationships:
            raise ValueError(
                f"Relationship already registered: {relationship.relationship_id}"
            )
        self._relationships[relationship.relationship_id] = relationship
        return relationship

    def register_mapping(self, mapping: SemanticMapping) -> SemanticMapping:
        self._mappings[mapping.source_term.strip().lower()] = mapping
        return mapping

    def get_concept(self, concept_id: str) -> SemanticConcept:
        try:
            return self._concepts[concept_id]
        except KeyError as exc:
            raise KeyError(concept_id) from exc

    def get_relationship(self, relationship_id: str) -> SemanticRelationship:
        try:
            return self._relationships[relationship_id]
        except KeyError as exc:
            raise KeyError(relationship_id) from exc

    def resolve_mapping(self, source_term: str) -> SemanticMapping | None:
        return self._mappings.get(source_term.strip().lower())

    def concepts(self) -> tuple[SemanticConcept, ...]:
        return tuple(self._concepts.values())
