from pydantic import BaseModel, Field
from pydantic.json_schema import SkipJsonSchema
from app.schemas.common import BaseResponse
from app.domain.models import VideoModelOut
from app.utils.custom_types import (
    URL_VALIDATOR,
    UUID_VALIDATOR
)


class VideosListOut(BaseResponse):
    data: list[VideoModelOut]


class VideoInput(BaseModel):
    user_uuid: SkipJsonSchema[str] = Field(default=None)
    video_url: URL_VALIDATOR = Field()
    video_uuid: UUID_VALIDATOR | None = Field(default=None)
