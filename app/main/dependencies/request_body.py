from app.main.exceptions import UnsupportedMediaType, RequiredRequestBody
from json.decoder import JSONDecodeError
from fastapi import Request


class RequestBody:
    CONTENT_TYPE_HEADER = "Content-Type"
    CONTENT_TYPE_VALUE = "application/json"

    async def __call__(self, request: Request):
        content_type = request.headers.get(self.CONTENT_TYPE_HEADER)

        if not content_type or not content_type.count(self.CONTENT_TYPE_VALUE):
            raise UnsupportedMediaType(self.CONTENT_TYPE_HEADER)

        try:
            body = await request.json()
        except JSONDecodeError:
            raise RequiredRequestBody()

        if not body:
            raise RequiredRequestBody()
