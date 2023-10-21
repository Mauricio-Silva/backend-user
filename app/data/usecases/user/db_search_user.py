from app.domain.usecases import SearchUser
from app.data.protocols import SearchUserRepository
from app.main.exceptions import NotFound


class DbSearchUser(SearchUser):
    def __init__(
        self,
        search_user_repository: SearchUserRepository
    ) -> None:
        self.__search_user_repository = search_user_repository

    async def search(self, data: str) -> SearchUser.Output:
        users = await self.__search_user_repository.search(data)

        if users is None:
            raise NotFound("User(s)")

        return users
