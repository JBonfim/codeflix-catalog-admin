from core.genre.domain.genre import Genre
from core.genre.infra.in_memory_genre_repository import InMemoryGenreRepository


class TestInMemoryGenreRepository:
    def test_can_save_Genre(self):
        repository = InMemoryGenreRepository()
        genre = Genre(
            name="Filme"
        )

        repository.save(genre)

        assert len(repository.genres) == 1
        assert repository.genres[0] == genre