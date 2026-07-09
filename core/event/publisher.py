from dataclasses import dataclass
from .contracts import Event, EventEnvelope

@dataclass
class PublisherMetrics:
    published:int=0
    failed:int=0
    duplicates:int=0
    serialization_errors:int=0
    validation_errors:int=0

class BasePublisher:
    def __init__(self):
        self.metrics=PublisherMetrics()

    def publish(self,event:Event)->EventEnvelope:
        env=EventEnvelope(event=event)
        self.metrics.published+=1
        return env

    def publish_many(self,events):
        return [self.publish(e) for e in events]

class InMemoryPublisher(BasePublisher):
    def __init__(self):
        super().__init__()
        self.published_events=[]

    def publish(self,event):
        env=super().publish(event)
        self.published_events.append(env)
        return env
