"""Module with the Entity service to serve"""
from app.core.db_repositories import BaseRepository

from .models import Entity, EntityDB
from .schemas import EntityUpdate

class EntityService:
    """Service to interact with entity collection.

    Args:
        entity_repo (BaseRepository): Repository for the DB connection
    """

    def __init__(self, entity_repo: BaseRepository) -> None:
        self.entity_repo = entity_repo

    async def get_entity(self, entity_id: str):
        return await self.entity_repo.get_by_id(entity_id)

    async def create_entity(self, entity: Entity):
        new_entity = EntityDB(**entity.dict())
        await self.entity_repo.save(new_entity)
        return new_entity

    async def update_entity(self, updated_entity: EntityUpdate):
        return await self.entity_repo.update(updated_entity)

    async def delete_entity(self, entity_id: str):
        await self.entity_repo.delete(entity_id)
