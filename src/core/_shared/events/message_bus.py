import logging
from typing import Type, List

from core._shared.events.abstract_message_bus import AbstractMessageBus
from core._shared.application.handlers import Handler
from core._shared.events.event import Event, TEvent
from core._shared.infrastructure.events.rabbitmq_dispatcher import RabbitMQDispatcher
from core.video.application.events.handlers import PublishAudioVideoMediaUpdatedHandler, DummyHandler
from core.video.application.events.integration_events import AudioVideoMediaUpdatedIntegrationEvent
from core.video.domain.events import AudioVideoMediaUpdated

logger = logging.getLogger(__name__)


class MessageBus(AbstractMessageBus):
    def __init__(self):
        self.handlers: dict[Type[TEvent], List[Handler[TEvent]]] = {
            AudioVideoMediaUpdatedIntegrationEvent: [
                PublishAudioVideoMediaUpdatedHandler(dispatcher=RabbitMQDispatcher(queue="videos.new")),
            ],
            AudioVideoMediaUpdated: [
                DummyHandler(),
            ],
        }

    def handle(self, events: list[Event]) -> None:
        for event in events:
            for handler in self.handlers[type(event)]:
                try:
                    handler.handle(event)
                except Exception:
                    logger.exception("Exception handling event %s", event)
                    continue