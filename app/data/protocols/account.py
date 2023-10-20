from abc import ABCMeta, abstractmethod
from app.domain.usecases import UpdatePassword


class GetPasswordByUuidRepository(metaclass=ABCMeta):
    @abstractmethod
    async def get_by_id(self, uuid: str) -> str:
        pass


class UpdatePasswordRepository(metaclass=ABCMeta):
    Input = UpdatePassword.Input

    @abstractmethod
    async def update_password(self, data: Input) -> None:
        pass
