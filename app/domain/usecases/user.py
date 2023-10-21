from pydantic import BaseModel
from app.domain.models import UserModelOut, ProfileModelOut, UserLoginModelOut
from abc import ABCMeta, abstractmethod


class ListUsers(metaclass=ABCMeta):
    Output = list[UserModelOut] | None

    @abstractmethod
    async def list_all(self) -> Output:
        pass


class PersonalProfile(metaclass=ABCMeta):
    Output = ProfileModelOut | None

    @abstractmethod
    async def get_personal_profile(self, uuid: str) -> Output:
        pass


class GetUserByUuid(metaclass=ABCMeta):
    Output = UserModelOut | None

    @abstractmethod
    async def get_by_id(self, uuid: str) -> Output:
        pass


class SearchUser(metaclass=ABCMeta):
    Output = list[UserModelOut] | None

    @abstractmethod
    async def search(self, data: str) -> Output:
        pass


class GetUserInput(BaseModel):
    username: str
    email: str | None = None


class GetUserByUnique(metaclass=ABCMeta):
    Input = GetUserInput
    Output = UserLoginModelOut | None

    @abstractmethod
    async def check_unique(self, data: Input) -> None:
        pass

    @abstractmethod
    async def get_by_unique(self, username_or_email: str) -> Output:
        pass


class CreateUserInput(BaseModel):
    name: str
    username: str
    email: str | None
    password: str
    phone: str | None
    bio: str | None


class CreateUser(metaclass=ABCMeta):
    Input = CreateUserInput
    Output = UserModelOut

    @abstractmethod
    async def create(self, data: Input) -> Output:
        pass


class UpdateUserInput(BaseModel):
    uuid: str
    name: str | None
    username: str | None
    email: str | None
    phone: str | None
    bio: str | None


class UpdateUser(metaclass=ABCMeta):
    Input = UpdateUserInput
    Output = UserModelOut | None

    @abstractmethod
    async def update(self, data: Input) -> Output:
        pass


class DeleteUser(metaclass=ABCMeta):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        pass


class EnableUser(metaclass=ABCMeta):
    Output = UserModelOut | None

    @abstractmethod
    async def enable(self, uuid: str) -> Output:
        pass


class DisableUser(metaclass=ABCMeta):
    Output = UserModelOut | None

    @abstractmethod
    async def disable(self, uuid: str) -> Output:
        pass
