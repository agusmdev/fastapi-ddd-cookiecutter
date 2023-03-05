"""Module with the models for the DB connection"""
from uuid import uuid4

from pydantic import BaseModel, Field


class Entity(BaseModel):
    name: str
    entity_field: int


class EntityDB(Entity):
    entity_id: str = Field(default_factory=lambda: uuid4().hex)

    class Config:
        orm_mode = True
