from dataclasses import dataclass
from uuid import UUID
from core.cast_member.domain.cast_member_repository import CastMemberRepository
from core.cast_member.application.user_cases.exceptions import InvalidCastMember

from core.cast_member.domain.cast_member import CastMember, CastMemberType


@dataclass
class CreateCastMemberRequest:
    name: str
    type: CastMemberType


@dataclass
class CreateCastMemberResponse:
    id: UUID


class CreateCastMember:
    def __init__(self, repository: CastMemberRepository):
        self.repository = repository

    def execute(self, request: CreateCastMemberRequest) -> CreateCastMemberResponse:
        try:
            cast_member = CastMember(
                name=request.name,
                type=request.type,
            )
        except ValueError as err:
            raise InvalidCastMember(err)

        self.repository.save(cast_member)
        return CreateCastMemberResponse(id=cast_member.id)
