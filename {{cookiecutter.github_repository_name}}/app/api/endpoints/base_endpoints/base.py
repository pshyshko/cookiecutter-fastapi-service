from http import HTTPStatus
from fastapi import APIRouter


base_api_router: APIRouter = APIRouter(tags=["Status"])


@base_endpoints.get("/status/ping", status_code=HTTPStatus.OK)
async def get_status():
    return "pong"