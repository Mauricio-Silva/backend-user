from fastapi import FastAPI
from app.main.config import Server
from app.utils import lifespan, Logger
from app.main.routes import ROUTES
from app.main.exceptions import ExceptionHandler
from app.main.middlewares import TraceControl
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    **Server.app,
    lifespan=lifespan,
    exception_handlers=ExceptionHandler.handlers()
)

app.add_middleware(TraceControl)
app.add_middleware(CORSMiddleware, **Server.origin)

for router in ROUTES:
    app.include_router(router)

Logger.info("\033[33mSnapcut Backend User Service was Initialized 🚀\033[m")
