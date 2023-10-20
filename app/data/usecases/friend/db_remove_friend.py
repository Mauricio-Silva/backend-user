from app.domain.usecases import RemoveFriend
from app.data.protocols import RemoveFriendRepository


class DbRemoveFriend(RemoveFriend):
    def __init__(
        self,
        remove_friend_repository: RemoveFriendRepository
    ) -> None:
        self.__remove_friend_repository = remove_friend_repository

    async def remove_friend(self, data: RemoveFriend.Input) -> None:
        return await self.__remove_friend_repository.remove_friend(data)
