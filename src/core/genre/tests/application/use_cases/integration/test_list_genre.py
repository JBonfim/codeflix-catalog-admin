from core.category.domain.category import Category
from core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from core.genre.application.user_cases.list_genre import ListGenre, GenreOutput
from core.genre.domain.genre import Genre
from core.genre.infra.in_memory_genre_repository import InMemoryGenreRepository


class TestListGenre:
    def test_list_genres_with_associated_categories(self):
        category_repository = InMemoryCategoryRepository()
        genre_repository = InMemoryGenreRepository()

        cat_1 = Category(name="Category 1", description="Category 1 description")
        category_repository.save(cat_1)

        cat_2 = Category(name="Category 2", description="Category 2 description")
        category_repository.save(cat_2)

        genre_drama = Genre(
            name="Drama",
            categories={cat_1.id, cat_2.id},
        )
        genre_repository.save(genre_drama)

        genre_romance = Genre(name="Romance")
        genre_repository.save(genre_romance)


        use_case = ListGenre(repository=genre_repository)
        output = use_case.execute(ListGenre.Input())

        assert output == ListGenre.Output(
            data=[
                GenreOutput(
                    id=genre_drama.id,
                    name="Drama",
                    categories={cat_1.id, cat_2.id},
                    is_active=True,
                ),
                GenreOutput(
                    id=genre_romance.id,
                    name="Romance",
                    categories=set(),
                    is_active=True,
                ),
            ]
        )