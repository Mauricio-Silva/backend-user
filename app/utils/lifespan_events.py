from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.main.config import ENVS
from app.infra.mongo import MongoConnection
# from app.infra.mongo import BackgroundTask
from .logger import Logger


@asynccontextmanager
async def lifespan(_: FastAPI):
    if not all(ENVS):
        message = "Environment Variables must be specified"
        Logger.error(message)
        raise ValueError(message)
    with MongoConnection() as _:
        pass
    Logger.info("\033[33mConnected to the MongoDB database\033[m")
    # background_task = BackgroundTask()
    # Logger.info("\033[33mNew Thread Running Background Task\033[m")
    yield
    # background_task.thread_shutdown()
    # Logger.info("\033[33mBackground Task Thread Stopped\033[m")
