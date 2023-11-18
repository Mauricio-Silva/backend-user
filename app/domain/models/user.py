from pydantic import BaseModel, ConfigDict, Field
from app.schemas.common import OBJECT_UUID, DATETIME, LIST


class UserModelOut(BaseModel):
    uuid: OBJECT_UUID = Field(validation_alias="_id")
    name: str | None = None
    username: str | None
    email: str | None
    photo: str | None = None
    phone: str | None = None
    bio: str | None
    create_at: DATETIME | None
    update_at: DATETIME | None
    verified_at: DATETIME | None = None
    is_enabled: bool | None = None

    model_config = ConfigDict(arbitrary_types_allowed=True)


class UserLoginModelOut(UserModelOut):
    password: str | None = None


class ProfileModelOut(BaseModel):
    uuid: OBJECT_UUID = Field(validation_alias="_id")
    name: str | None = None
    username: str | None
    email: str | None
    photo: str | None = None
    phone: str | None = None
    bio: str | None
    videos: LIST = None
    friends: LIST = None

    model_config = ConfigDict(arbitrary_types_allowed=True)
