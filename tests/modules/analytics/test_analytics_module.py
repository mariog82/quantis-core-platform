from modules.analytics import AnalyticsModule


def test_analytics_module_lifecycle_and_calculation():
    module = AnalyticsModule()

    module.initialize(context={})
    module.boot()
    module.start()

    result = module.calculate("active_users", {"active_users": 12})

    assert module.initialized is True
    assert module.started is True
    assert result.value == 12
