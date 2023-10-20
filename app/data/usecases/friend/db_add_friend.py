from app.domain.usecases import AddFriend
from app.data.protocols import AddFriendRepository


class DbAddFriend(AddFriend):
    def __init__(
        self,
        add_friend_repository: AddFriendRepository
    ) -> None:
        self.__add_friend_repository = add_friend_repository

    async def add_friend(self, data: AddFriend.Input) -> None:
        return await self.__add_friend_repository.add_friend(data)
