from pydantic import BaseModel, Field
from pydantic.json_schema import SkipJsonSchema
from app.schemas.common import BaseResponse
from app.domain.models import LoginModelOut
from app.utils.custom_types import (
    PASSWORD_VALIDATOR,
    EMAIL_VALIDATOR
)


class UserLogin(BaseModel):
    username_or_email: str = Field(..., min_length=6, max_length=70)
    password: PASSWORD_VALIDATOR = Field(..., min_length=6, max_length=20)


class LoginOut(BaseResponse):
    data: LoginModelOut


class PasswordUpdate(BaseModel):
    uuid: SkipJsonSchema[str | None] = Field(default=None)
    old_password: PASSWORD_VALIDATOR = Field(..., min_length=6, max_length=20)
    new_password: PASSWORD_VALIDATOR = Field(..., min_length=6, max_length=20)


class PasswordReset(BaseModel):
    email: EMAIL_VALIDATOR = Field(..., min_length=6, max_length=70)
