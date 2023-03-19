"""This module is the temporary solution until pydantic V2 is out, with support to forcing all models' fields to be optional"""

from typing import Mapping, Any, List, Type, Optional
from pydantic import BaseModel


def model_annotations_with_parents(model: BaseModel) -> Mapping[str, Any]:
    parent_models: List[Type] = [
        parent_model
        for parent_model in model.__bases__
        if (issubclass(parent_model, BaseModel) and hasattr(parent_model, "__annotations__"))
    ]

    annotations: Mapping[str, Any] = {}

    for parent_model in reversed(parent_models):
        annotations.update(model_annotations_with_parents(parent_model))

    annotations.update(model.__annotations__)
    return annotations


def optional_model_factory(model: BaseModel, name: str = None) -> BaseModel:

    return type(
        name,
        (model,),
        dict(
            __module__=model.__module__,
            __annotations__={
                k: Optional[v] for k, v in model_annotations_with_parents(model).items()
            },
        ),
    )


def optional_model(cls: BaseModel) -> BaseModel:
    return optional_model_factory(cls, name=cls.__name__)
