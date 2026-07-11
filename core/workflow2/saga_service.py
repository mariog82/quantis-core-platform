from core.workflow2.saga import SagaDefinition, SagaEngine, SagaInstance
from core.workflow2.saga_repository import SagaRepository


class SagaService:
    def __init__(
        self,
        engine: SagaEngine,
        repository: SagaRepository,
    ) -> None:
        self.engine = engine
        self.repository = repository

    def execute(
        self,
        definition: SagaDefinition,
        context: dict | None = None,
    ) -> SagaInstance:
        instance = self.repository.save(
            self.engine.start(definition, context)
        )
        result = self.engine.run(instance)
        return self.repository.save(result)
