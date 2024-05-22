from app.api.endpoints.base_endpoints.base import base_endpoints
from app.core.config import service_settings
from fastapi import APIRouter


union_route = APIRouter()
union_route.include_router(base_api_router)
