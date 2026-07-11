import types
from tools.public_api_integrity.checks import _has_all, _public_symbols_exist

def test_public_api_helpers():
    module = types.SimpleNamespace(__all__=["Existing", "Missing"], Existing=object())
    assert _has_all(module) is True
    assert _public_symbols_exist(module) == ["Missing"]
