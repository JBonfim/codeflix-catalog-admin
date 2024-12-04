import unittest
from uuid import UUID
import pytest
from category import Category

class TestCategory():
    
    def test_name_is_required(self):
        with pytest.raises(TypeError):
            Category()
    def test_name_must_les_than_255_caractes(self):
        with pytest.raises(ValueError,match="name must have less than 255 caracteres"):
            Category(name="a"*256)
            
    def test_create_category_with_id_as_uuid_by_default(self):
        category = Category(name="filme")
        assert isinstance(category.id,UUID)
        
    def test_create_category_with_default_values(self):
        category = Category(name="filme")
        assert category.name == "filme"
        assert category.description == ""
        assert category.is_active == True
    
    def test_name_is_not_empty(self):
        with pytest.raises(ValueError,match="name cannot by empty"):
            Category(name="")
    
    
class TestUpdateCategoy:
    def test_update_category_with_name_and_description(self):
        category = Category(name="filme",description="filme em geral")
        category.update_category("series",description="series em geral")
        
        assert category.name == "series"
        assert category.description == "series em geral"
        
    def test_update_category_with_name_and_description_must_les_than_255_caractes(self):
        category = Category(name="filme",description="filme em geral")
        
        with pytest.raises(ValueError,match="name must have less than 255 caracteres"):
            category.update_category("a"*256,description="series em geral")

