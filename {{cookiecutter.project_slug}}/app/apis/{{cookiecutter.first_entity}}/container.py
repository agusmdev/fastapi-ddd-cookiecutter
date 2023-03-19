"""Module to provide the containers with injected services for the app"""

from dependency_injector import containers, providers

from app.apis.entity.models import EntityDB
from app.apis.entity.service import EntityService


class EntityContainer(containers.DeclarativeContainer):
    """Container to serve the Entity service with the configured repository"""

    # Configuration to use
    config = providers.Configuration()

    repository = providers.Dependency()
    # Configure repository to use
    entity_repository = providers.Singleton(
        repository,
        model=EntityDB,
    )

    # Configure service with repository
    entity_service = providers.Singleton(EntityService, entity_repo=entity_repository)
