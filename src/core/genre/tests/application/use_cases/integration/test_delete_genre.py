from core.genre.application.user_cases.delete_genre import DeleteGenre
from core.genre.domain.genre import Genre
from core.genre.infra.in_memory_genre_repository import InMemoryGenreRepository


class TestDeleteGenre:
    def test_delete_genre_from_repository(self):
        genre = Genre(name="Drama")
        genre_repository = InMemoryGenreRepository()
        genre_repository.save(genre)
        use_case = DeleteGenre(repository=genre_repository)

        assert genre_repository.get_by_id(genre.id) == genre
        use_case.execute(DeleteGenre.Input(id=genre.id))
        assert genre_repository.get_by_id(genre.id) is None