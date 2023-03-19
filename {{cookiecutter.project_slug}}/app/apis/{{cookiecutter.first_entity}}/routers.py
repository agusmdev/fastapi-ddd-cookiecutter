"""Module with the routers related to the entity service"""
from typing import List
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, HTTPException, status

from .schemas import EntityCreate, EntityResponse, EntityUpdate
from .service import EntityService


@inject
def get_entity_router(entity_service: EntityService = Provide["entity_container.entity_service"]):
    router = APIRouter()

    @router.post(
        "",
        response_description="Add new entity",
        status_code=status.HTTP_201_CREATED,
    )
    async def create_entity(
        entity: EntityCreate = Body(...),
    ) -> EntityResponse:
        return await entity_service.create_entity(entity)

    @router.get(
        "",
        response_description="Get all the created entities",
        status_code=status.HTTP_200_OK,
    )
    async def get_all_entitys() -> List[EntityResponse]:
        return await entity_service.get_all_entitys()

    @router.get(
        "/{entity_id}",
        response_description="Get a single entity",
        status_code=status.HTTP_200_OK,
    )
    async def get_entity(
        entity_id: str,
    ) -> EntityResponse:
        entity = await entity_service.get_entity(entity_id)
        if not entity:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Entity {entity_id} not found",
            )

        return entity

    @router.patch(
        "/{entity_id}",
        response_description="Update entity",
        status_code=status.HTTP_202_ACCEPTED,
    )
    async def update_entity(entity_id: str, entity: EntityUpdate = Body(...)) -> None:
        await entity_service.update_entity(entity_id, entity)

    @router.delete(
        "/{entity_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        response_description="Delete entity",
    )
    async def delete_entity(
        entity_id: str,
    ) -> None:
        await entity_service.delete_entity(entity_id)

    return router
