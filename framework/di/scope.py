from enum import Enum


class DependencyScope(str, Enum):
    INSTANCE = "INSTANCE"
    SINGLETON = "SINGLETON"
    FACTORY = "FACTORY"
