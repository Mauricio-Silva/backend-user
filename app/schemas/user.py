from pydantic import BaseModel, Field
from pydantic.json_schema import SkipJsonSchema
from app.schemas.common import BaseResponse
from app.domain.models import UserModelOut, ProfileModelOut
from app.utils.custom_types import (
    NAME_VALIDATOR,
    USERNAME_VALIDATOR,
    EMAIL_VALIDATOR,
    PASSWORD_VALIDATOR,
    BIO_VALIDATOR
)


class UserOut(BaseResponse):
    data: UserModelOut


class UsersOut(BaseResponse):
    data: list[UserModelOut]


class ProfileOut(BaseResponse):
    data: ProfileModelOut


class UserCreate(BaseModel):
    name: NAME_VALIDATOR = Field(...)
    username: USERNAME_VALIDATOR = Field(...)
    email: EMAIL_VALIDATOR | None = Field(default=None)
    password: PASSWORD_VALIDATOR = Field(...)
    bio: BIO_VALIDATOR | None = Field(default=None)


class UserUpdate(BaseModel):
    uuid: SkipJsonSchema[str | None] = Field(default=None)
    name: NAME_VALIDATOR | None = Field(default=None)
    username: USERNAME_VALIDATOR | None = Field(default=None)
    email: EMAIL_VALIDATOR | None = Field(default=None)
    bio: BIO_VALIDATOR | None = Field(default=None)
