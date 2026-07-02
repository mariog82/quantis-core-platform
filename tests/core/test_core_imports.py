def test_core_packages_importable():
    import core.identity
    import core.tenant
    import core.rbac
    import core.audit
    import core.eventbus
    import core.configuration
    import core.observability

    assert core.identity is not None
    assert core.tenant is not None
    assert core.rbac is not None
    assert core.audit is not None
    assert core.eventbus is not None
    assert core.configuration is not None
    assert core.observability is not None
