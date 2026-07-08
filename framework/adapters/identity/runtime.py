class IdentityProviderRuntime:
    def __init__(self, adapter):
        self.adapter = adapter
    def validate_token(self, request):
        return self.adapter.validate_token(request)
    def lookup_user(self, request):
        return self.adapter.lookup_user(request)
