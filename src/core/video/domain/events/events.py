from dataclasses import dataclass
from uuid import UUID

from core._shared.events.event import Event
from core.video.domain.value_objects import MediaType


@dataclass(frozen=True)
class AudioVideoMediaUpdated(Event):
    aggregate_id: UUID
    media_type: MediaType
    file_path: str