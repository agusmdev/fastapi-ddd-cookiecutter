"""Module with the models for the DB connection"""
from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import uuid4

from pydantic import BaseModel, Field, validator


class EntitySize(str, Enum):
    MEDIUM = "Mediano"
    BIG = "Grande"
    SMALL = "Chico"


class EntitySex(str, Enum):
    MALE = "Macho"
    FEMALE = "Hembra"


class EntityType(str, Enum):
    DOG = "Perro"
    CAT = "Gato"


class Entity(BaseModel):
    ask_adoption: Optional[bool] = True
    ask_temporary: Optional[bool] = True
    birthdate: Optional[datetime] = None
    name: Optional[str] = None
    photos: Optional[List[str]]
    verification_ids: Optional[List]
    location_hash: str = None  # TODO
    location_lat: float
    location_lng: float
    entity_sex: EntitySex
    entity_size: EntitySize
    entity_type: EntityType

    @validator("birthdate")
    def validate_birthdate(cls, v):
        return v.isoformat() if v else None


class EntityDB(Entity):
    entity_id: str = Field(default_factory=lambda: uuid4().hex)
