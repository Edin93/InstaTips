import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.database import database

# from api.logging_conf import configure_logging
from api.routers.post import router as post_router
from api.routers.user import router as user_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # configure_logging()
    logger.info("hello world")
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(post_router)
app.include_router(user_router)
