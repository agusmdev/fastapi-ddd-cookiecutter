"""Unit testing for app.apis.entity.repositories"""

from app.apis.entity.models import EntityDB
from app.apis.repositories import get_repository, str_to_class
from app.core.db_repositories import InMemoryRepository


def test_str_to_class():
    assert str_to_class("InMemoryRepository") == InMemoryRepository
    assert str_to_class("NotExistingClass") is None
    assert str_to_class("BaseModel") is None  # Only valid repositories


def test_get_repository():
    assert isinstance(
        get_repository("InMemoryRepository", "entity_id", "table", EntityDB),
        InMemoryRepository,
    )
    assert get_repository("not_supported_db", "entity_id", "table", EntityDB) == None
