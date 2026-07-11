from core.workflow2 import (
    SagaActionResult,
    SagaDefinition,
    SagaEngine,
    SagaStatus,
    SagaStep,
)


class Executor:
    def execute(self, action, context):
        return SagaActionResult(
            success=True,
            output={action: True},
        )

    def compensate(self, compensation, context):
        return SagaActionResult(success=True)


def test_saga_completes_all_steps():
    definition = SagaDefinition(
        saga_type="tenant.provisioning",
        version=1,
        steps=(
            SagaStep("create", "create-tenant", "delete-tenant"),
            SagaStep("license", "assign-license", "revoke-license"),
        ),
    )

    result = SagaEngine(Executor()).run(
        SagaEngine(Executor()).start(definition)
    )

    assert result.status == SagaStatus.COMPLETED
    assert result.completed_steps == ("create", "license")
    assert result.context["create-tenant"] is True
    assert result.context["assign-license"] is True
