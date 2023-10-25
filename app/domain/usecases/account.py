from pydantic import BaseModel
from abc import ABCMeta, abstractmethod


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
    username: str
    url: str | None = None


class ResetPassword(metaclass=ABCMeta):
    Input = ResetPasswordInput

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


class CheckUserEmailInput(BaseModel):
    uuid: str
    email: str
    username: str
    url: str | None = None


class CheckUserEmail(metaclass=ABCMeta):
    Input = CheckUserEmailInput

    @abstractmethod
    async def verify_email(self, data: Input) -> None:
        pass


class ValidateUserEmail(metaclass=ABCMeta):
    @abstractmethod
    async def validate_email(self, uuid: str) -> None:
        pass
