import pytest


from core.category.domain.category import Category
from django_project.category_app.repository import DjangoORMCategoryRepository
from django_project.genre_app.models import Genre as GenreORM
from core.genre.domain.genre import Genre
from django_project.genre_app.repository import DjangoORMGenreRepository


@pytest.mark.django_db
class TestSave:
    def test_saves_genre_in_database(self):
        genre = Genre(name="Movie")
        repository = DjangoORMGenreRepository()

        assert GenreORM.objects.count() == 0
        repository.save(genre)
        assert GenreORM.objects.count() == 1
        saved_category = GenreORM.objects.get()

        assert saved_category.id == genre.id
        assert saved_category.name == genre.name
        assert saved_category.is_active == genre.is_active

    def test_saves_genre_with_related_categories_in_database(self):
        repository = DjangoORMGenreRepository()
        category_repository = DjangoORMCategoryRepository()

        category = Category(name="Action")
        category_repository.save(category)

        genre = Genre(name="Movie")
        genre.add_category(category.id)

        assert GenreORM.objects.count() == 0
        repository.save(genre)
        assert GenreORM.objects.count() == 1

        saved_genre = GenreORM.objects.get()
        assert saved_genre.categories.count() == 1

        related_category = saved_genre.categories.get()
        assert related_category.id == category.id