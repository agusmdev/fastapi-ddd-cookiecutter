"""Module with the Entity service to serve"""
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

    async def get_entity(self, entity_id: str):
        return self.entity_repo.get_by(entity_id).first()

    async def create_entity(self, entity: Entity):
        new_entity = EntityDB(**entity.dict())
        self.entity_repo.add(new_entity)
        return new_entity

    async def update_entity(self, updated_entity: EntityUpdate):
        self.entity_repo.update(updated_entity)

    async def delete_entity(self, entity_id: str):
        self.entity_repo.get_by(entity_id).delete()
