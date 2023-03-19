"""Unit testing for app.apis.entity.routers"""
# pylint: disable=redefined-outer-name

import pytest
import pytest_asyncio

from app.apis.entity.models import EntityDB
from pydantic_factories import ModelFactory


class EntityDBFactory(ModelFactory):
    __model__ = EntityDB


mocked_entitys = EntityDBFactory.batch(10)


@pytest_asyncio.fixture(scope="module", autouse=True)
async def mocked_repo(app):
    repo = app.container.entity_container.entity_repository()
    _ = [repo.add(mocked_entity) for mocked_entity in mocked_entitys]
    return repo


@pytest.mark.asyncio
async def test_get_entity_exists(client):
    for entity in mocked_entitys:
        entity_id = entity.entity_id
        response = await client.get(
            f"/entitys/{entity_id}",
        )
        assert response.status_code == 200
        result = response.json()
        assert EntityDB(**result) == entity


@pytest.mark.asyncio
async def test_get_entity_not_exists(client):
    not_valid_entity_id = "9132687213"
    response = await client.get(
        f"/entitys/{not_valid_entity_id}",
    )
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_get_all_entitys(client):
    response = await client.get("/entitys")
    assert response.status_code == 200
    all_entitys = [EntityDB(**entity) for entity in response.json()]
    assert sorted(mocked_entitys, key=lambda x: x.entity_id) == sorted(all_entitys, key=lambda x: x.entity_id)


@pytest.mark.asyncio
async def test_create_entity(client, mocked_repo):
    for entity in mocked_entitys:
        new_entity = entity.dict()
        new_entity.pop("entity_id")

        response = await client.post(
            "/entitys",
            json=new_entity,
        )
        new_entity_id = response.json()["entity_id"]
        assert response.status_code == 201
        created_entity = mocked_repo.filter_by(entity_id=new_entity_id).first()
        assert created_entity is not None


@pytest.mark.asyncio
async def test_update_entity(client, mocked_repo):
    for entity in mocked_entitys:
        entity_id = entity.entity_id

        response = await client.patch(
            f"/entitys/{entity_id}",
            json={"entity_id": entity_id, "entity_field": 999},
        )
        assert response.status_code == 202
        updated_entity = mocked_repo.filter_by(entity_id=entity_id).first()
        assert updated_entity.entity_field == 999


@pytest.mark.asyncio
async def test_delete_entity(client, mocked_repo):
    for entity in mocked_entitys:
        entity_id = entity.entity_id

        existing_entity = mocked_repo.filter_by(entity_id=entity_id).first()
        assert existing_entity is not None

        response = await client.delete(f"/entitys/{entity_id}")
        assert response.status_code == 204

        removed_entity = mocked_repo.filter_by(entity_id=entity_id).first()
        assert removed_entity is None


@pytest.mark.asyncio
async def test_sanity_check(client):
    response = await client.get(
        "/sanity-check",
    )

    assert response.status_code == 200
    data = response.json()
    assert data == "FastAPI running!"
