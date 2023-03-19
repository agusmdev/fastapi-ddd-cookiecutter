"""Module with the models for the DB connection"""
from enum import Enum
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field


class Status(str, Enum):
    STATUS_1 = "1"
    STATUS_2 = "2"
    STATUS_3 = "3"
    STATUS_4 = "4"


class Entity(BaseModel):
    name: str
    entity_field: int
    random_field: Optional[str] = None
    status: Status


class EntityDB(Entity):
    __colname__ = "entitys"
    __id_field__ = "entity_id"

    entity_id: str = Field(default_factory=lambda: uuid4().hex)
