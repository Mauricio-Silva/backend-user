from abc import ABCMeta, abstractmethod
from app.domain.models import VideoModelOut


class ListVideos(metaclass=ABCMeta):
    Output = list[VideoModelOut] | None

    @abstractmethod
    async def list_all(self) -> Output:
        pass


class ListMyVideos(metaclass=ABCMeta):
    Output = list[VideoModelOut] | None

    @abstractmethod
    async def list_my_videos(self, uuid: str) -> Output:
        pass


class ListFriendsVideos(metaclass=ABCMeta):
    Output = list[VideoModelOut] | None

    @abstractmethod
    async def list_friends_videos(self, uuid: str) -> Output:
        pass
