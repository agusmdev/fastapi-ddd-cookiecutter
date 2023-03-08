"""Module to provide repositories for the pet service"""

import sys
from typing import Type, Union

import redbird.repos
from redbird.templates import TemplateRepo


def str_to_class(classname: str) -> Union[Type[TemplateRepo], None]:
    """Get a Python class corresponding to the string input. It only works with
     classes that are subclasses of `TemplateRepo`, otherwise it returns None.

    Args:
        classname (str): Name of class to get.

    Returns:
        Union[Type[TemplateRepo], None]: Valid repository class,
         or None if the input doesn't correspond to a valid class.
    """
    try:
        class_ = getattr(sys.modules[redbird.repos.__name__], classname)
        assert issubclass(class_, TemplateRepo)
        return class_
    except (AttributeError, AssertionError):
        return None


def get_repository(db_class: str, *args, **kwargs) -> Union[Type[TemplateRepo], None]:
    """Get an instantiated repository, or None if the repository indicated
     was not found. The rest of arguments are passed to the repository constructor.

    Args:
        db_class (str): Name of the class of the repository to instantiate.

    Returns:
        Union[Type[TemplateRepo], None]: Valid repository created,
         or None if the input doesn't correspond to a valid class.
    """
    db = str_to_class(db_class)
    if db is not None:
        return db(*args, **kwargs)
    return None