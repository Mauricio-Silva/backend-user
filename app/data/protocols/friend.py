from abc import ABCMeta, abstractmethod
from app.domain.usecases import (
    ListFriends,
    AddFriend,
    RemoveFriend
)


class ListFriendsRepository(metaclass=ABCMeta):
    Output = ListFriends.Output

    @abstractmethod
    async def list_all(self, uuid: str) -> Output:
        pass


class AddFriendRepository(metaclass=ABCMeta):
    Input = AddFriend.Input

    @abstractmethod
    async def add_friend(self, data: Input) -> None:
        pass


class RemoveFriendRepository(metaclass=ABCMeta):
    Input = RemoveFriend.Input

    @abstractmethod
    async def remove_friend(self, data: Input) -> None:
        pass
