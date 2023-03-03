"""Module with schemas for the DB connection"""

from .models import Entity, EntityDB


class EntityCreate(Entity):
    ...


class EntityResponse(EntityDB):
    ...
