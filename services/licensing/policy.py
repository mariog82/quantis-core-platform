from services.licensing.entitlement import Entitlement, EntitlementDecision
from services.licensing.license import License, LicenseStatus


class LicensePolicy:
    def evaluate(self, license: License | None, entitlement: Entitlement) -> EntitlementDecision:
        if license is None:
            return EntitlementDecision(allowed=False, reason="LICENSE_NOT_FOUND")

        if license.status != LicenseStatus.ACTIVE:
            return EntitlementDecision(allowed=False, reason=f"LICENSE_{license.status.value.upper()}")

        if entitlement.feature not in license.features:
            return EntitlementDecision(allowed=False, reason="FEATURE_NOT_LICENSED")

        limit = license.limit_for(entitlement.feature)
        if limit is not None and entitlement.quantity > limit:
            return EntitlementDecision(
                allowed=False,
                reason="FEATURE_LIMIT_EXCEEDED",
                metadata={"limit": limit, "requested": entitlement.quantity},
            )

        return EntitlementDecision(allowed=True)
