from dataclasses import dataclass, field
from uuid import UUID

from core.genre.domain.genre_repository import GenreRepository


@dataclass
class GenreOutput:
    id: UUID
    name: str
    categories: set[UUID]
    is_active: bool
    
@dataclass
class ListOutputMeta:
   current_page: int
   per_page : int
   total: int


class ListGenre:
    def __init__(self, repository: GenreRepository):
        self.repository = repository

    @dataclass
    class Input:
        order_by: str = "name"  # Desafio: ordenação decrescente? ASC/DESC
        current_page: int = 1

    @dataclass
    class Output:
        data: list[GenreOutput]
        meta: ListOutputMeta = field(default_factory=ListOutputMeta)

    def execute(self, input: Input) -> Output:
        genres = self.repository.list()
        
        sorted_genres = sorted(
        [
           GenreOutput(
                id=genre.id,
                name=genre.name,
                categories=genre.categories,
                is_active=genre.is_active,
            ) for genre in genres
        ],
        key=lambda genre: getattr(genre, input.order_by))
        
        DEFAULT_PAGE_SIZE = 2
        page_offset = (input.current_page - 1) * DEFAULT_PAGE_SIZE
        genres_page = sorted_genres[page_offset:page_offset + DEFAULT_PAGE_SIZE]
        

        return self.Output(
            data=genres_page,
            meta=ListOutputMeta(
                current_page=input.current_page,
                per_page=DEFAULT_PAGE_SIZE,
                total=len(genres),
            ),
        )