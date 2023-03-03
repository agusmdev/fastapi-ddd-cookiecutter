"""Module for including all the app's routers"""
from fastapi import APIRouter

from app.apis.entity.routers import get_entity_router


def get_app_router():
    router = APIRouter()
    router.include_router(get_entity_router(), prefix="/entitys", tags=["entitys"])

    return router
