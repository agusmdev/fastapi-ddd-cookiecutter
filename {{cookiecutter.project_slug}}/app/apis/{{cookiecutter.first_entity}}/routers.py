"""Module with the routers related to the entity service"""
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
        response_model=EntityResponse,
        status_code=status.HTTP_201_CREATED,
    )
    async def create_entity(
        entity: EntityCreate = Body(...),
    ):
        return await entity_service.create_entity(entity)

    @router.get(
        "/{entity_id}",
        response_description="Get a single entity",
        response_model=EntityResponse,
        status_code=status.HTTP_200_OK,
    )
    async def get_entity(
        entity_id: str,
    ):
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
        response_model=EntityResponse,
    )
    async def update_entity(entity_id: str, entity: EntityUpdate = Body(...)):
        try:
            return await entity_service.update_entity(entity)
        except Exception:  # Update to named exception
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Entity {entity.entity_id} not found",
            )

    @router.delete(
        "/{entity_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        response_description="Delete entity",
    )
    async def delete_entity(
        entity_id: str,
    ):
        await entity_service.delete_entity(entity_id)

    return router
