from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.main.config import Lifespan
from .logger import Logger
from pymongo.mongo_client import MongoClient
# import webbrowser


@asynccontextmanager
async def lifespan(_: FastAPI):
    check_db = bool(Lifespan.docker) or all(Lifespan.db_envs)
    if not all(Lifespan.envs) and check_db:
        raise ValueError("Environment Variables must be specified")
    client = MongoClient(Lifespan.mongo)
    try:
        client.admin.command('ping')
    except Exception:
        raise ConnectionError("Cannot connect to Mongo Database")
    finally:
        client.close()
    # webbrowser.get(Lifespan.browser).open(Lifespan.swagger)
    Logger.info("\033[33mConnected to the MongoDB database\033[m")
    yield
