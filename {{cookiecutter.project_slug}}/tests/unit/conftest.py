from asyncio import get_event_loop

import pytest_asyncio
from dependency_injector import providers
from httpx import AsyncClient

from app.apis.containers import AppContainer
from app.apis.repositories import get_repository
from app.main import create_app


@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def app():
    container = AppContainer(
        repository=providers.Singleton(get_repository, "MemoryRepo"),
    )
    yield create_app(container)


@pytest_asyncio.fixture(scope="module")
async def client(app):
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c
