from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan_with_database(app: FastAPI):
    yield


service = FastAPI(
    docs_url="/docs",
    lifespan=lifespan_with_database,
)