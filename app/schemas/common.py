from pydantic import BaseModel, PlainSerializer, WithJsonSchema
from typing import Annotated, Callable, Awaitable
from starlette.responses import Response
from fastapi import Request, Path, Query
from datetime import datetime
from bson import ObjectId
from app.utils.serializations import (
    serialize_object_id,
    serialize_datetime,
    serialize_list
)
from app.utils.custom_types import (
    UUID_VALIDATOR,
    SEARCH_VALIDATOR
)


OBJECT_UUID = Annotated[
    ObjectId,
    PlainSerializer(serialize_object_id, return_type=str, when_used='always'),
    WithJsonSchema({'type': 'string'}, mode='serialization')
]
DATETIME = Annotated[
    datetime,
    PlainSerializer(serialize_datetime, return_type=str, when_used='always'),
    WithJsonSchema({'type': 'string'}, mode='serialization')
]
LIST = Annotated[
    list | None,
    PlainSerializer(serialize_list, return_type=int, when_used='always'),
]


PATH_UUID = Annotated[UUID_VALIDATOR, Path(description="UUID")]
QUERY_SEARCH = Annotated[SEARCH_VALIDATOR, Query(alias="search", description="Name or Username")]
ACCOUNT_SEARCH = Annotated[SEARCH_VALIDATOR, Query(alias="search", description="Email")]
CALL_NEXT_RESPONSE = Callable[[Request], Awaitable[Response]]


class BaseResponse(BaseModel):
    message: str
    success: bool = True


class MessageResponse(BaseResponse):
    pass
