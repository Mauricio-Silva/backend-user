from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.main.config import Lifespan
from .logger import Logger
from pymongo.mongo_client import MongoClient
# import webbrowser


@asynccontextmanager
async def lifespan(_: FastAPI):
    if not all(Lifespan.envs):
        raise ValueError("Database Environment Variables must be specified")
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
