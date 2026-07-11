from core.workflow2 import (
    SagaActionResult,
    SagaDefinition,
    SagaEngine,
    SagaStatus,
    SagaStep,
)


class Executor:
    def execute(self, action, context):
        if action == "assign-license":
            return SagaActionResult(
                success=False,
                error="license failure",
            )
        return SagaActionResult(
            success=True,
            output={"tenant_created": True},
        )

    def compensate(self, compensation, context):
        return SagaActionResult(
            success=True,
            output={compensation: True},
        )


def test_saga_compensates_completed_steps_in_reverse_order():
    definition = SagaDefinition(
        saga_type="tenant.provisioning",
        version=1,
        steps=(
            SagaStep("create", "create-tenant", "delete-tenant"),
            SagaStep("license", "assign-license", "revoke-license"),
        ),
    )
    engine = SagaEngine(Executor())

    result = engine.run(engine.start(definition))

    assert result.status == SagaStatus.COMPENSATED
    assert result.completed_steps == ("create",)
    assert result.compensated_steps == ("create",)
    assert result.context["delete-tenant"] is True
