"""Unit testing for app.apis.entity.repositories"""

from app.apis.entity.models import EntityDB
from app.apis.repositories import get_repository, str_to_class
from redbird.repos import MemoryRepo


def test_str_to_class():
    assert str_to_class("MemoryRepo") == MemoryRepo
    assert str_to_class("NotExistingClass") is None
    assert str_to_class("BaseModel") is None  # Only valid repositories


def test_get_repository():
    assert isinstance(
        get_repository("MemoryRepo", id_field="entity_id", model=EntityDB),
        MemoryRepo,
    )
    assert get_repository("not_supported_db", "entity_id", EntityDB) == None
