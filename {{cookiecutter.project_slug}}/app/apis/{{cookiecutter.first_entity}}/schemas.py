"""Module with schemas for transforming data from requests and responses"""

from app.core.model_factory import optional_model
from .models import Entity, EntityDB


class EntityCreate(Entity):
    ...


@optional_model
class EntityUpdate(Entity):
    ...


class EntityResponse(EntityDB):
    ...
