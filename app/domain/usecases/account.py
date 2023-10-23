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
    access_token: str | None = None


class ResetPassword(metaclass=ABCMeta):
    Input = ResetPasswordInput

    @abstractmethod
    async def reset_password(self, data: Input) -> None:
        pass
