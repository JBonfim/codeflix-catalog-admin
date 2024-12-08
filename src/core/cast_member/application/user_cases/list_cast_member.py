from dataclasses import dataclass
from uuid import UUID
from core.cast_member.domain.cast_member import CastMemberType
from core.cast_member.domain.cast_member_repository import CastMemberRepository

@dataclass
class CastMemberOutput:
    id: UUID
    name: str
    type: CastMemberType

@dataclass
class ListOutputMeta:
   current_page: int
   per_page : int
   total: int

@dataclass
class ListCastMemberRequest:
    order_by: str = "name"  # Desafio: ordenação decrescente? ASC/DESC
    current_page: int = 1


@dataclass
class ListCastMemberResponse:
    data: list[CastMemberOutput]


class ListCastMember:
    def __init__(self, repository: CastMemberRepository) -> None:
        self.repository = repository

    def execute(self, request: ListCastMemberRequest) -> ListCastMemberResponse:
        cast_members = self.repository.list()
        
        sorted_cast_members = sorted(
        [
            CastMemberOutput(
                 id=cast_member.id,
                 name=cast_member.name,
                 type=cast_member.type,
            ) for cast_member in cast_members
        ],
        key=lambda cast_member: getattr(cast_member, request.order_by))
        
        DEFAULT_PAGE_SIZE = 2
        page_offset = (request.current_page - 1) * DEFAULT_PAGE_SIZE
        cast_members_page = sorted_cast_members[page_offset:page_offset + DEFAULT_PAGE_SIZE]

        return ListCastMemberResponse(
            data=cast_members_page,
            meta=ListOutputMeta(
                current_page=request.current_page,
                per_page=DEFAULT_PAGE_SIZE,
                total=len(cast_members),
            ),
        )