class GraphCoreException(Exception):
    pass

class InvalidGraphElement(GraphCoreException):
    pass

class DuplicateNode(GraphCoreException):
    pass

class DuplicateEdge(GraphCoreException):
    pass

class NodeNotFound(GraphCoreException):
    pass

class EdgeNotFound(GraphCoreException):
    pass
