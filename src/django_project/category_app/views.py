from uuid import UUID
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
    HTTP_201_CREATED,
)

from core.category.application.user_cases.create_category import CreateCategory, CreateCategoryRequest
from core.category.application.user_cases.delete_category import DeleteCategory, DeleteCategoryRequest
from core.category.application.user_cases.exceptions import CategoryNotFound
from core.category.application.user_cases.get_category import GetCategory, GetCategoryRequest
from core.category.application.user_cases.list_category import ListCategory, ListCategoryRequest, ListCategoryResponse
from core.category.application.user_cases.update_category import UpdateCategory, UpdateCategoryRequest
from django_project.category_app.repository import DjangoORMCategoryRepository
from django_project.category_app.serializers import CreateCategoryRequestSerializer, CreateCategoryResponseSerializer, DeleteCategoryRequestSerializer, ListCategoryResponseSerializer, RetrieveCategoryRequestSerializer, RetrieveCategoryResponseSerializer, UpdateCategoryRequestSerializer

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
    def list(self, request: Request) -> Response:
        order_by = request.query_params.get("order_by", "name")
        use_case = ListCategory(repository=DjangoORMCategoryRepository())
        output: ListCategoryResponse = use_case.execute(request=ListCategoryRequest(
            order_by=order_by,
            current_page=int(request.query_params.get("current_page", 1)),
        ))
        response_serializer = ListCategoryResponseSerializer(output)

        return Response(
            status=HTTP_200_OK,
            data=response_serializer.data,
        )

    def retrieve(self, request: Request, pk: UUID = None) -> Response:
        serializer = RetrieveCategoryRequestSerializer(data={"id": pk})
        serializer.is_valid(raise_exception=True)

        input = GetCategoryRequest(**serializer.validated_data)
        use_case = GetCategory(repository=DjangoORMCategoryRepository())

        try:
            output = use_case.execute(request=input)
        except CategoryNotFound:
            return Response(status=HTTP_404_NOT_FOUND)

        response_serializer = RetrieveCategoryResponseSerializer(output)
        return Response(
            status=HTTP_200_OK,
            data=response_serializer.data,
        )

    def create(self, request: Request) -> Response:
        serializer = CreateCategoryRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        input = CreateCategoryRequest(**serializer.validated_data)
        use_case = CreateCategory(repository=DjangoORMCategoryRepository())
        output = use_case.execute(request=input)

        return Response(
            status=HTTP_201_CREATED,
            data=CreateCategoryResponseSerializer(output).data,
        )

    def update(self, request: Request, pk: UUID = None):
        serializer = UpdateCategoryRequestSerializer(data={
            **request.data,
            "id": pk,
        })
        serializer.is_valid(raise_exception=True)

        input = UpdateCategoryRequest(**serializer.validated_data)
        use_case = UpdateCategory(repository=DjangoORMCategoryRepository())
        try:
            use_case.execute(request=input)
        except CategoryNotFound:
            return Response(status=HTTP_404_NOT_FOUND)

        return Response(status=HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk: UUID = None):
        serializer = UpdateCategoryRequestSerializer(data={
            **request.data,
            "id": pk,
        }, partial=True)
        serializer.is_valid(raise_exception=True)

        input = UpdateCategoryRequest(**serializer.validated_data)
        use_case = UpdateCategory(repository=DjangoORMCategoryRepository())
        try:
            use_case.execute(request=input)
        except CategoryNotFound:
            return Response(status=HTTP_404_NOT_FOUND)

        return Response(status=HTTP_204_NO_CONTENT)

    def destroy(self, request: Request, pk: UUID = None):
        request_data = DeleteCategoryRequestSerializer(data={"id": pk})
        request_data.is_valid(raise_exception=True)

        input = DeleteCategoryRequest(**request_data.validated_data)
        use_case = DeleteCategory(repository=DjangoORMCategoryRepository())
        try:
            use_case.execute(input)
        except CategoryNotFound:
            return Response(status=HTTP_404_NOT_FOUND)

        return Response(status=HTTP_204_NO_CONTENT)