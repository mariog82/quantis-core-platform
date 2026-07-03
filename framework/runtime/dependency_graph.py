class DependencyGraph:

    def __init__(self):

        self.dependencies = {}

    def add(self, module, depends_on):

        self.dependencies[module] = depends_on

    def dependencies_of(self, module):

        return self.dependencies.get(module, [])

    def validate(self):

        return True