from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.main.config import Lifespan
from app.infra.mongo import MongoConnection
# from app.infra.mongo import BackgroundTask
from .logger import Logger
# import webbrowser


@asynccontextmanager
async def lifespan(_: FastAPI):
    if not all(Lifespan.envs):
        message = "Environment Variables must be specified"
        Logger.error(message)
        raise ValueError(message)
    with MongoConnection() as _:
        pass
    # webbrowser.get(Lifespan.browser).open(Lifespan.swagger)
    Logger.info("\033[33mConnected to the MongoDB database\033[m")
    # background_task = BackgroundTask()
    # Logger.info("\033[33mNew Thread Running Background Task\033[m")
    yield
    # background_task.thread_shutdown()
    # Logger.info("\033[33mBackground Task Thread Stopped\033[m")
