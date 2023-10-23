from abc import ABCMeta, abstractmethod
from app.domain.usecases import (
    UpdatePassword,
    ResetPassword
)


class GetPasswordByUuidRepository(metaclass=ABCMeta):
    @abstractmethod
    async def get_by_id(self, uuid: str) -> str:
        pass


class UpdatePasswordRepository(metaclass=ABCMeta):
    Input = UpdatePassword.Input

    @abstractmethod
    async def update_password(self, data: Input) -> None:
        pass


class ResetPasswordRepository(metaclass=ABCMeta):
    Input = ResetPassword.Input

    @abstractmethod
    async def reset_password(self, data: Input) -> None:
        pass
