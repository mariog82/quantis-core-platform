from framework.contracts.module import BaseModule, ModuleManifest
from framework.contracts.plugin import BasePlugin, PluginManifest
from framework.di import DependencyContainer
from framework.plugins import PluginRuntime
from framework.runtime import RuntimeContext, RuntimeKernel, RuntimeManager
from framework.workflow import Workflow, WorkflowContext, WorkflowEngine, WorkflowId, WorkflowStep


class DemoService:
    def value(self) -> str:
        return "ok"


class DemoModule(BaseModule):
    manifest = ModuleManifest(name="demo-module", version="0.1.0", capabilities=["demo"])

    def __init__(self):
        self.started = False
        self.service = None

    def initialize(self, context):
        self.service = context.resolve_dependency(DemoService)

    def boot(self):
        pass

    def start(self):
        self.started = True

    def stop(self):
        self.started = False

    def shutdown(self):
        pass


class DemoPlugin(BasePlugin):
    manifest = PluginManifest(name="demo-plugin", version="0.1.0")


def test_runtime_di_plugin_workflow_integration():
    container = DependencyContainer()
    container.register_singleton(DemoService, DemoService)

    context = RuntimeContext(container=container)
    manager = RuntimeManager(context=context)
    module = DemoModule()
    manager.register(module)

    kernel = RuntimeKernel(manager)
    kernel.boot()
    kernel.initialize()
    kernel.start()

    assert module.started is True
    assert module.service.value() == "ok"

    plugins = PluginRuntime()
    plugins.install(DemoPlugin())
    plugins.enable("demo-plugin")

    def workflow_step(workflow_context: WorkflowContext) -> WorkflowContext:
        workflow_context.data["module_started"] = module.started
        workflow_context.data["plugin_enabled"] = plugins.registry.get("demo-plugin").status == "enabled"
        return workflow_context

    workflow = Workflow(id=WorkflowId(), name="integration-workflow")
    workflow.add_step(WorkflowStep(name="collect-runtime-state", handler=workflow_step))

    engine = WorkflowEngine()
    engine.register(workflow)
    execution = engine.execute("integration-workflow")

    assert execution.context.data["module_started"] is True
    assert execution.context.data["plugin_enabled"] is True
