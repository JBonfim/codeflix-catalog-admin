from uuid import UUID

import pytest


from src.core.category.application.user_cases.create_category import create_category
from src.core.category.application.user_cases.exceptions import InvalidCategory

class TestCreateCategory:
    def test_create_category(self):
        category_id = create_category(name="filme",description="teste desc",is_active=True)
        
        assert category_id  is not None
        assert isinstance(category_id,UUID)  
        
    def test_create_category_with_invalid_data(self):
        
        with pytest.raises(InvalidCategory,match="name cannot by empty") as exc_info:
            category_id = create_category(name="")
        
        assert exc_info.type is InvalidCategory
        assert str(exc_info.value) == "name cannot by empty"