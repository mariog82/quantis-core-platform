from framework.adapters.identity.adapter import IdentityProviderAdapter
from framework.adapters.identity.contracts import (
    IdentityTokenValidationRequest,
    IdentityTokenValidationResponse,
    IdentityUserLookupRequest,
    IdentityUserLookupResponse,
)


class IdentityProviderRuntime:
    def __init__(self, adapter: IdentityProviderAdapter):
        self.adapter = adapter

    def validate_token(self, request: IdentityTokenValidationRequest) -> IdentityTokenValidationResponse:
        return self.adapter.validate_token(request)

    def lookup_user(self, request: IdentityUserLookupRequest) -> IdentityUserLookupResponse:
        return self.adapter.lookup_user(request)
