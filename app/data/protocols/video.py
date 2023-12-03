from abc import ABCMeta, abstractmethod
from app.domain.usecases import (
    ListVideos,
    ListMyVideos,
    ListFriendsVideos
)


class ListVideosRepository(metaclass=ABCMeta):
    Output = ListVideos.Output

    @abstractmethod
    async def list_all(self) -> Output:
        pass


class ListMyVideosRepository(metaclass=ABCMeta):
    Output = ListMyVideos.Output

    @abstractmethod
    async def list_my_videos(self, uuid: str) -> Output:
        pass


class ListFriendsVideosRepository(metaclass=ABCMeta):
    Output = ListFriendsVideos.Output

    @abstractmethod
    async def list_friends_videos(self, uuid: str) -> Output:
        pass
