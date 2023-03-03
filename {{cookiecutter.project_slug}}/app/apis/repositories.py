"""Module to provide repositories for the entity service"""

import sys
from typing import Type, Union

from app.core import db_repositories


def str_to_class(classname: str) -> Union[Type[db_repositories.BaseRepository], None]:
    """Get a Python class corresponding to the string input. It only works with
     classes that are subclasses of `BaseRepository`, otherwise it returns None.

    Args:
        classname (str): Name of class to get.

    Returns:
        Union[Type[db_repositories.BaseRepository], None]: Valid repository class,
         or None if the input doesn't correspond to a valid class.
    """
    try:
        class_ = getattr(sys.modules[db_repositories.__name__], classname)
        assert issubclass(class_, db_repositories.BaseRepository)
        return class_
    except (AttributeError, AssertionError):
        return None


def get_repository(
    db_class: str, *args, **kwargs
) -> Union[Type[db_repositories.BaseRepository], None]:
    """Get an instantiated repository, or None if the repository indicated
     was not found. The rest of arguments are passed to the repository constructor.

    Args:
        db_class (str): Name of the class of the repository to instantiate.

    Returns:
        Union[Type[db_repositories.BaseRepository], None]: Valid repository created,
         or None if the input doesn't correspond to a valid class.
    """
    db = str_to_class(db_class)
    if db is not None:
        return db(*args, **kwargs)
    return None
