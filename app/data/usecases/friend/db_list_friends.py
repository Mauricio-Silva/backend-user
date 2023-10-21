from app.domain.usecases import ListFriends
from app.data.protocols import ListFriendsRepository
from app.main.exceptions import NotFound


class DbListFriends(ListFriends):
    def __init__(
        self,
        list_friends_repository: ListFriendsRepository
    ) -> None:
        self.__list_friends_repository = list_friends_repository

    async def list_all(self, uuid: str) -> ListFriends.Output:
        friends = await self.__list_friends_repository.list_all(uuid)

        if not friends:
            raise NotFound("Friends")

        return friends
