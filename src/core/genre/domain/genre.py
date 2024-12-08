from dataclasses import dataclass, field
import uuid
from typing import Set
from uuid import UUID

from core._shared.domain.entity import Entity


@dataclass
class Genre(Entity):
    name: str
    is_active: bool = True
    categories: Set[UUID] = field(default_factory=set)

    def __post_init__(self):
        self.validate()

    def validate(self):
        if len(self.name) > 255:
            # raise ValueError("name cannot be longer than 255")
            self.notification.add_error("name cannot be longer than 255")

        if not self.name:
            self.notification.add_error("name cannot be empty")
            # raise ValueError("name cannot be empty")
            
        if self.notification.has_errors:
            # Não interrompemos o fluxo e acumulamos os erros
            # Poderíamos não retornar `ValueError` e deixar como responsabilidade do cliente verificar se há erros.
            raise ValueError(self.notification.messages)
        

    def __str__(self):
        return f"{self.name} (active: {self.is_active})"

    def __repr__(self):
        return f"<Genre {self.name} ({self.id})>"

    def __eq__(self, other):
        if not isinstance(other, Genre):
            return False

        return self.id == other.id

    def add_category(self, category_id: UUID) -> None:
        self.categories.add(category_id)
        self.validate()

    def remove_category(self, category_id: UUID) -> None:
        self.categories.remove(category_id)
        self.validate()

    def update_categories(self, category_ids: Set[UUID]) -> None:
        self.categories = category_ids
        self.validate()

    def change_name(self, name):
        self.name = name
        self.validate()

    def activate(self):
        self.is_active = True
        self.validate()

    def deactivate(self):
        self.is_active = False
        self.validate()