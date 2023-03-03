"""Module to provide the containers with injected services for the app"""

from dependency_injector import containers, providers

from app.apis.entity import routers as entity_router
from app.apis.entity.container import EntityContainer
from app.apis.repositories import get_repository

from .config import settings


class AppContainer(containers.DeclarativeContainer):
    """Container to serve all the containers related to the app"""

    # Set wiring between endpoints and injected repositories
    wiring_config = containers.WiringConfiguration(modules=[entity_router])
    # Set configuration for the app
    config = providers.Configuration()
    # Setup container for entity services
    repository = providers.Singleton(get_repository, settings.REPOSITORY_NAME)

    entity_container = providers.Container(
        EntityContainer,
        repository=repository,
        config=config,
    )
