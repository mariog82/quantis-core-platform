class ModuleRegistry:

    def __init__(self):

        self.modules = {}

    def register(self, module):

        self.modules[module.manifest.name] = module

    def unregister(self, name):

        self.modules.pop(name, None)

    def get(self, name):

        return self.modules.get(name)

    def list(self):

        return list(self.modules.values())

    def exists(self, name):

        return name in self.modules