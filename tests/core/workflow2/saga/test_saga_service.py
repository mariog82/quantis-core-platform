from core.workflow2 import (
    InMemorySagaRepository,
    SagaActionResult,
    SagaDefinition,
    SagaEngine,
    SagaService,
    SagaStatus,
    SagaStep,
)


class Executor:
    def execute(self, action, context):
        return SagaActionResult(success=True)

    def compensate(self, compensation, context):
        return SagaActionResult(success=True)


def test_saga_service_persists_result():
    repository = InMemorySagaRepository()
    service = SagaService(
        SagaEngine(Executor()),
        repository,
    )
    definition = SagaDefinition(
        saga_type="simple",
        version=1,
        steps=(SagaStep("one", "run"),),
    )

    result = service.execute(definition)

    assert result.status == SagaStatus.COMPLETED
    assert repository.get(result.saga_id) == result
