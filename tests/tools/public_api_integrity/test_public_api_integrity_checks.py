import types

from tools.public_api_integrity.checks import _has_all, _public_symbols_exist


def test_has_all_accepts_non_empty_all():
    module = types.SimpleNamespace(__all__=["Example"], Example=object())

    assert _has_all(module) is True


def test_public_symbols_exist_detects_broken_exports():
    module = types.SimpleNamespace(__all__=["Existing", "Missing"], Existing=object())

    assert _public_symbols_exist(module) == ["Missing"]
