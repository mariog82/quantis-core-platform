from .publisher import InMemoryPublisher

class PublisherFactory:
    @staticmethod
    def create(name:str="memory"):
        return InMemoryPublisher()
