from starlette.middleware.base import BaseHTTPMiddleware
from app.schemas.common import CALL_NEXT_RESPONSE
from app.utils import Logger
from fastapi import Request
import traceback
import http
import time


class TraceControl(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: CALL_NEXT_RESPONSE):
        url = f"{request.url.path}?{request.query_params}" if request.query_params else request.url.path
        start_time = time.time()

        try:
            response = await call_next(request)
        except Exception as exception:
            Logger.exception(exception)
            traceback.print_exc()
            raise exception

        end_time = (time.time() - start_time) * 1000
        status_phrase = http.HTTPStatus(response.status_code).phrase
        process_time = "{0:.2f}".format(end_time)
        host = request.client.host or "0.0.0.0"
        port = request.client.port or 8000

        Logger.trace(host, port, request.method, url, response.status_code, status_phrase, process_time)

        return response
