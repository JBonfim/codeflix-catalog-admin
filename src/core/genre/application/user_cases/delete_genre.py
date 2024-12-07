from dataclasses import dataclass
from uuid import UUID

from core.genre.application.user_cases.exceptions import GenreNotFound
from core.genre.domain.genre_repository import GenreRepository


class DeleteGenre:
    @dataclass
    class Input:
        id: UUID

    def __init__(self, repository: GenreRepository):
        self.repository = repository

    def execute(self, input: Input) -> None:
        genre = self.repository.get_by_id(input.id)

        if genre is None:
            raise GenreNotFound(f"Genre with id {input.id} not found")

        self.repository.delete(id=input.id)