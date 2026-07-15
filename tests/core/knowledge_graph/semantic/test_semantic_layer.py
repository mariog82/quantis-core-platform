from core.knowledge_graph import (
    SemanticConcept,
    SemanticInferenceEngine,
    SemanticLayerService,
    SemanticMapping,
    SemanticNormalizer,
    SemanticRegistry,
    SemanticRelationship,
)


def test_registry_normalizer_and_mapping():
    registry = SemanticRegistry()
    concept = registry.register_concept(
        SemanticConcept(
            "documento_amministrativo",
            "Documento amministrativo",
            aliases=("atto amministrativo",),
        )
    )
    registry.register_mapping(
        SemanticMapping("delibera", concept.concept_id)
    )
    assert registry.resolve_mapping("DELIBERA") is not None
    assert SemanticNormalizer().normalize("Delibéra") == "delibera"


def test_hierarchy_and_inverse_inference():
    service = SemanticLayerService()
    service.add_concept(SemanticConcept("documento", "Documento"))
    service.add_concept(
        SemanticConcept(
            "delibera",
            "Delibera",
            parent_ids=("documento",),
        )
    )
    service.add_concept(
        SemanticConcept("organo_collegiale", "Organo collegiale")
    )
    service.registry.register_relationship(
        SemanticRelationship(
            "approva",
            "Approva",
            "organo_collegiale",
            "delibera",
        )
    )
    service.add_relationship(
        SemanticRelationship(
            "approvata_da",
            "Approvata da",
            "delibera",
            "organo_collegiale",
            inverse_id="approva",
        )
    )
    inferred = SemanticInferenceEngine().infer_concept_hierarchy(
        "delibera-001",
        "delibera",
        service.registry,
    )
    inverse = service.inference_engine.infer_inverse_relationship(
        "delibera-001",
        "approvata_da",
        "consiglio-001",
        service.registry,
    )
    assert inferred[0].object_id == "documento"
    assert inverse is not None
    assert inverse.predicate == "approva"
