from pydantic import BaseModel
from abc import ABCMeta, abstractmethod
from app.domain.models import UserModelOut


class UpdatePasswordInput(BaseModel):
    uuid: str
    old_password: str
    new_password: str


class UpdatePassword(metaclass=ABCMeta):
    Input = UpdatePasswordInput

    @abstractmethod
    async def update_password(self, data: Input) -> None:
        pass


class ResetPasswordInput(BaseModel):
    email: str


class UserEmailInput(BaseModel):
    to: str
    subject: str
    username: str
    link: str


class ResetPassword(metaclass=ABCMeta):
    Input = ResetPasswordInput
    Email = UserEmailInput

    @abstractmethod
    async def reset_password(self, data: Input) -> None:
        pass


class SetNewPasswordInput(BaseModel):
    uuid: str
    password: str


class SetNewPassword(metaclass=ABCMeta):
    Input = SetNewPasswordInput

    @abstractmethod
    async def set_new_password(self, data: Input) -> None:
        pass


class CheckUserEmail(metaclass=ABCMeta):
    Input = UserModelOut
    Email = UserEmailInput

    @abstractmethod
    async def verify_email(self, data: Input) -> None:
        pass


class ValidateUserEmail(metaclass=ABCMeta):
    Output = UserModelOut | None

    @abstractmethod
    async def validate_email(self, uuid: str) -> Output:
        pass
