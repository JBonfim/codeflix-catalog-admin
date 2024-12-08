
from dataclasses import dataclass, field
from uuid import UUID

from core.category.domain.category_repository import CategoryRepository


@dataclass
class CategoryOutput:
    id: UUID
    name: str
    description: str
    is_active: bool


@dataclass
class ListCategoryRequest:
    order_by: str = "name"  # Desafio: ordenação decrescente? ASC/DESC
    current_page: int = 1
    
@dataclass
class ListOutputMeta:
   current_page: int
   per_page : int
   total: int


@dataclass
class ListCategoryResponse:
    data: list[CategoryOutput]
    meta: ListOutputMeta = field(default_factory=ListOutputMeta)


class ListCategory:
    def __init__(self, repository: CategoryRepository) -> None:
        self.repository = repository

    def execute(self, request: ListCategoryRequest) -> ListCategoryResponse:
        categories = self.repository.list()
        sorted_categories = sorted(
        [
            CategoryOutput(
                id=category.id,
                name=category.name,
                description=category.description,
                is_active=category.is_active,
            ) for category in categories
        ],
        key=lambda category: getattr(category, request.order_by))
        
        DEFAULT_PAGE_SIZE = 2
        page_offset = (request.current_page - 1) * DEFAULT_PAGE_SIZE
        categories_page = sorted_categories[page_offset:page_offset + DEFAULT_PAGE_SIZE]


        return ListCategoryResponse(
            data=categories_page,
            meta=ListOutputMeta(
                current_page=request.current_page,
                per_page=DEFAULT_PAGE_SIZE,
                total=len(categories),
            ),
        )