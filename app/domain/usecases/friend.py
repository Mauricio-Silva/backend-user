from pydantic import BaseModel
from abc import ABCMeta, abstractmethod


class ListFriends(metaclass=ABCMeta):
    Output = list[str] | None

    @abstractmethod
    async def list_all(self, uuid: str) -> Output:
        pass


class AddOrRemoveFriendInput(BaseModel):
    user_uuid: str
    friend_uuid: str


class AddFriend(metaclass=ABCMeta):
    Input = AddOrRemoveFriendInput

    @abstractmethod
    async def add_friend(self, data: Input) -> None:
        pass


class RemoveFriend(metaclass=ABCMeta):
    Input = AddOrRemoveFriendInput

    @abstractmethod
    async def remove_friend(self, data: Input) -> None:
        pass
