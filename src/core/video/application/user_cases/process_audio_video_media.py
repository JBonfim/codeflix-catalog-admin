from dataclasses import dataclass
from decimal import Decimal
from typing import Set
from uuid import UUID

from core._shared.domain.notification import Notification
from core.cast_member.domain.cast_member_repository import CastMemberRepository
from core.category.domain.category_repository import CategoryRepository
from core.genre.domain.genre_repository import GenreRepository
from core.video.application.user_cases.exceptions import MediaNotFound, VideoNotFound
from core.video.domain.value_objects import Rating, MediaType, MediaStatus
from core.video.domain.video import Video
from core.video.domain.video_repository import VideoRepository


class ProcessAudioVideoMedia:
    @dataclass
    class Input:
        video_id: UUID
        encoded_location: str
        media_type: MediaType
        status: MediaStatus

    def __init__(self, video_repository: VideoRepository) -> None:
        self._video_repository = video_repository

    def execute(self, request: Input) -> None:
        video = self._video_repository.get_by_id(request.video_id)
        if video is None:
            raise VideoNotFound(f"Video with id {request.video_id} not found")

        if request.media_type == MediaType.VIDEO:
            if not video.video:
                raise MediaNotFound("Video must have a video media to be processed")
            
            print("Iniciando o processo do video")

            video.process(status=request.status, encoded_location=request.encoded_location)

        self._video_repository.update(video)