class GraphAlgorithmException(Exception):
    pass


class AlgorithmNodeNotFound(GraphAlgorithmException):
    pass


class NegativeWeightNotSupported(GraphAlgorithmException):
    pass


class GraphContainsCycle(GraphAlgorithmException):
    pass
