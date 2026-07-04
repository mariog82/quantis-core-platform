from framework.contracts.module import BaseModule, ModuleManifest
from modules.reporting.defaults import create_default_report_catalog
from modules.reporting.service import ReportingModuleService


class ReportingModule(BaseModule):
    manifest = ModuleManifest(
        name="reporting",
        version="0.3.0-alpha.6",
        description="Reusable reporting module foundation.",
        capabilities=["reporting", "export", "templates"],
        dependencies=["analytics"],
    )

    def __init__(self):
        self.initialized = False
        self.started = False
        self.service = ReportingModuleService()
        for template in create_default_report_catalog().list_templates():
            self.service.register_template(template)

    def initialize(self, context):
        self.context = context
        self.initialized = True

    def boot(self):
        pass

    def start(self):
        self.started = True

    def stop(self):
        self.started = False

    def shutdown(self):
        self.started = False

    def generate(self, template_key: str, data: dict) -> bytes:
        return self.service.generate(template_key, data)
