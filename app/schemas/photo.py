from pydantic import BaseModel, Field
from pydantic.json_schema import SkipJsonSchema
from app.utils.custom_types import URL_VALIDATOR
from enum import Enum


class OperationType(Enum):
    ADDED = 'added'
    UPDATED = 'updated'
    REMOVED = 'removed'


class PhotoInput(BaseModel):
    user_uuid: SkipJsonSchema[str] = Field(default=None)
    photo_url: URL_VALIDATOR = Field(default=None)
