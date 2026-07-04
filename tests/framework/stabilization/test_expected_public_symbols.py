def test_runtime_public_symbols():
    from framework.runtime import RuntimeContext, RuntimeKernel, RuntimeManager

    assert RuntimeContext is not None
    assert RuntimeKernel is not None
    assert RuntimeManager is not None


def test_api_public_symbols():
    from framework.api import BaseController, RequestContext, ResponseBuilder

    assert BaseController is not None
    assert RequestContext is not None
    assert ResponseBuilder is not None


def test_persistence_public_symbols():
    from framework.persistence import InMemoryRepository, UnitOfWork

    assert InMemoryRepository is not None
    assert UnitOfWork is not None


def test_plugin_public_symbols():
    from framework.plugins import PluginRegistry, PluginRuntime

    assert PluginRegistry is not None
    assert PluginRuntime is not None


def test_workflow_public_symbols():
    from framework.workflow import Workflow, WorkflowEngine, WorkflowStep

    assert Workflow is not None
    assert WorkflowEngine is not None
    assert WorkflowStep is not None


def test_dashboard_public_symbols():
    from framework.dashboard import Dashboard, DashboardRuntime, DashboardWidget

    assert Dashboard is not None
    assert DashboardRuntime is not None
    assert DashboardWidget is not None


def test_reporting_public_symbols():
    from framework.reporting import ReportDefinition, ReportingRuntime, TextReportRenderer

    assert ReportDefinition is not None
    assert ReportingRuntime is not None
    assert TextReportRenderer is not None
