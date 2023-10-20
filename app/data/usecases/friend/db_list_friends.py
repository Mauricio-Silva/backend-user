from app.domain.usecases import ListFriends
from app.data.protocols import ListFriendsRepository


class DbListFriends(ListFriends):
    def __init__(
        self,
        list_friends_repository: ListFriendsRepository
    ) -> None:
        self.__list_friends_repository = list_friends_repository

    async def list_all(self, uuid: str) -> ListFriends.Output:
        return await self.__list_friends_repository.list_all(uuid)
