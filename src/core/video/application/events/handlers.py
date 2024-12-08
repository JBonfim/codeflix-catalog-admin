from core._shared.application.handlers import Handler
from core._shared.events.event_dispatcher import EventDispatcher
from core.video.application.events.integration_events import AudioVideoMediaUpdatedIntegrationEvent
from core.video.domain.events.events import AudioVideoMediaUpdated


class PublishAudioVideoMediaUpdatedHandler(Handler[AudioVideoMediaUpdatedIntegrationEvent]):
    def __init__(self, dispatcher: EventDispatcher):
        print("calling rabbitmq init")
        self.dispatcher = dispatcher

    def handle(self, event: AudioVideoMediaUpdatedIntegrationEvent) -> None:
        print(f"Dispatching integration event {event}")
        self.dispatcher.dispatch(event)


class DummyHandler(Handler[AudioVideoMediaUpdated]):
    def handle(self, event: AudioVideoMediaUpdated) -> None:
        print(f"Handling domain event {event} with DummyHandler")