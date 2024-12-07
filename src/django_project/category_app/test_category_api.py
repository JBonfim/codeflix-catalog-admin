from django.test import TestCase
import pytest
from rest_framework.test import APITestCase
from django_project.category_app.repository import DjangoORMCategoryRepository
from rest_framework.test import APIClient
from rest_framework import status
from core.category.domain.category import Category

# Create your tests here.
# class TestCategoryAPI(APITestCase):
#     def test_list_categories(self):
#         url = "/api/categories/"
#         response = self.client.get(url)
        
#         expected_data = [
#              {
#             "id": 1,
#             "description": "Produto 1",
#             "name": "filme",
#             "valor": 18396.2,
#             "is_active": "ATIVO"
#             },
#             {
#                 "id": 2,
#                 "description": "Produto2",
#                 "name": "filme",
#                 "valor": 19576.2,
#                 "is_active": "ATIVO"
#             }
#         ]
        
#         self.assertEqual(response.status_code,200)
#         self.assertEqual(response.data,expected_data)
        
@pytest.mark.django_db
class TestCategoryAPI:
    @pytest.fixture
    def category_movie(self):
        return  Category(
            name="Movie",
            description="Movie description",
        )

    @pytest.fixture
    def category_documentary(self):
        return Category(
            name="Documentary",
            description="Documentary description",
        )

    @pytest.fixture
    def category_repository(self) -> DjangoORMCategoryRepository:
        return DjangoORMCategoryRepository()

    def test_list_categories(
        self,
        category_movie: Category,
        category_documentary: Category,
        category_repository: DjangoORMCategoryRepository,
    ) -> None:
        category_repository.save(category_movie)
        category_repository.save(category_documentary)

        url = '/api/categories/'
        response = APIClient().get(url)
        
        expected_data = [
            {
                "id": str(category_movie.id),
                "name": "Movie",
                "description": "Movie description",
                "is_active": True
            },
            {
                "id": str(category_documentary.id),
                "name": "Documentary",
                "description": "Documentary description",
                "is_active": True
            }
        ]
        
        #print(response.data)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data == expected_data