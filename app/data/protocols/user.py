from abc import ABCMeta, abstractmethod
from app.domain.usecases import (
    ListUsers,
    PersonalProfile,
    GetUserByUuid,
    SearchUser,
    GetUserByUnique,
    CreateUser,
    UpdateUser,
    EnableUser,
    DisableUser
)


class ListUsersRepository(metaclass=ABCMeta):
    Output = ListUsers.Output

    @abstractmethod
    async def list_all(self) -> Output:
        pass


class PersonalProfileRepository(metaclass=ABCMeta):
    Output = PersonalProfile.Output

    @abstractmethod
    async def get_personal_profile(self, uuid: str) -> Output:
        pass


class GetUserByUuidRepository(metaclass=ABCMeta):
    Output = GetUserByUuid.Output

    @abstractmethod
    async def get_by_id(self, uuid: str) -> Output:
        pass


class SearchUserRepository(metaclass=ABCMeta):
    Output = SearchUser.Output

    @abstractmethod
    async def search(self, data: str) -> Output:
        pass


class GetUserByUniqueRepository(metaclass=ABCMeta):
    Input = GetUserByUnique.Input
    Output = GetUserByUnique.Output

    @abstractmethod
    async def check_unique(self, data: Input) -> None:
        pass

    @abstractmethod
    async def get_by_unique(self, username_or_email: str) -> Output:
        pass


class CreateUserRepository(metaclass=ABCMeta):
    Input = CreateUser.Input
    Output = CreateUser.Output

    @abstractmethod
    async def create(self, data: Input) -> Output:
        pass


class UpdateUserRepository(metaclass=ABCMeta):
    Input = UpdateUser.Input
    Output = UpdateUser.Output

    @abstractmethod
    async def update(self, data: Input) -> Output:
        pass


class DeleteUserRepository(metaclass=ABCMeta):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        pass


class EnableUserRepository(metaclass=ABCMeta):
    Output = EnableUser.Output

    @abstractmethod
    async def enable(self, uuid: str) -> Output:
        pass


class DisableUserRepository(metaclass=ABCMeta):
    Output = DisableUser.Output

    @abstractmethod
    async def disable(self, uuid: str) -> Output:
        pass
