from abc import ABCMeta, abstractmethod
from app.domain.usecases import (
    ListVideos,
    AddVideo,
    RemoveVideo,
    ListMyVideos,
    ListFriendsVideos
)


class ListVideosRepository(metaclass=ABCMeta):
    Output = ListVideos.Output

    @abstractmethod
    async def list_all(self) -> Output:
        pass


class AddVideoRepository(metaclass=ABCMeta):
    Input = AddVideo.Input

    @abstractmethod
    async def add_video(self, data: Input) -> None:
        pass


class RemoveVideoRepository(metaclass=ABCMeta):
    Input = RemoveVideo.Input

    @abstractmethod
    async def remove_video(self, data: Input) -> None:
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
