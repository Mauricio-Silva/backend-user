from pydantic import BaseModel, Field
from app.schemas.common import BaseResponse
from app.domain.models import AccountOut, LoginModelOut
from app.utils.custom_types import EMAIL_VALIDATOR


class EmailResend(BaseModel):
    email: EMAIL_VALIDATOR = Field(..., min_length=6, max_length=70)


class AccountsOut(BaseResponse):
    data: list[AccountOut]


class AccountLogin(BaseModel):
    username_or_email: str = Field(..., min_length=6, max_length=70)


class LoginOut(BaseResponse):
    data: LoginModelOut
