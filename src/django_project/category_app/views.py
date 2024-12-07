from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK

from core.category.application.user_cases.list_category import ListCategory, ListCategoryRequest
from django_project.category_app.repository import DjangoORMCategoryRepository

# Create your views here.

# class CategoryViewSet(viewsets.ViewSet):
#     def list(self, request: Request) -> Response:
#         return Response(status=HTTP_200_OK, data=[
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
#         ])



# Create your views here.

class CategoryViewSet(viewsets.ViewSet):
    def list(self, request: Request):
        use_case = ListCategory(repository=DjangoORMCategoryRepository())
        response = use_case.execute(request=ListCategoryRequest())

        categories = [
            {
                "id": str(category.id),
                "name": category.name,
                "description": category.description,
                "is_active": category.is_active,
            }
            for category in response.data
        ]

        return Response(
            status=HTTP_200_OK,
            data=categories,
        )
