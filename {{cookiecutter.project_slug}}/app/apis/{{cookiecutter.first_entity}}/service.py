"""Module with the Entity service to serve"""
from typing import List, Optional
from redbird.templates import TemplateRepo

from .models import Entity, EntityDB
from .schemas import EntityUpdate


class EntityService:
    """Service to interact with entity collection.

    Args:
        entity_repo (TemplateRepo): Repository for the DB connection
    """

    def __init__(self, entity_repo: TemplateRepo) -> None:
        self.entity_repo = entity_repo

    async def get_entity(self, entity_id: str) -> Optional[EntityDB]:
        return self.entity_repo.filter_by(entity_id=entity_id).first()

    async def get_all_entitys(self) -> List[EntityDB]:
        return self.entity_repo.filter_by().all()

    async def create_entity(self, entity: Entity) -> EntityDB:
        new_entity = EntityDB(**entity.dict())
        self.entity_repo.add(new_entity)
        return new_entity

    async def update_entity(self, entity_id: str, updated_entity: EntityUpdate) -> None:
        self.entity_repo.filter_by(entity_id=entity_id).update(**updated_entity.dict(exclude_unset=True))

    async def delete_entity(self, entity_id: str) -> None:
        self.entity_repo.filter_by(entity_id=entity_id).delete()
