from app.domain.usecases import ListUsers
from app.data.protocols import ListUsersRepository
from app.main.exceptions import NotFound


class DbListUsers(ListUsers):
    def __init__(
        self,
        list_users_repository: ListUsersRepository
    ) -> None:
        self.__list_users_repository = list_users_repository

    async def list_all(self) -> ListUsers.Output:
        users = await self.__list_users_repository.list_all()

        if not users:
            raise NotFound("Users")

        return users
