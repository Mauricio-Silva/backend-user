from pydantic import BaseModel
from abc import ABCMeta, abstractmethod
from app.domain.models import VideoModelOut


class ListVideos(metaclass=ABCMeta):
    Output = list[VideoModelOut] | None

    @abstractmethod
    async def list_all(self) -> Output:
        pass


class AddOrRemoveVideoInput(BaseModel):
    user_uuid: str
    video_url: str
    video_uuid: str | None


class AddVideo(metaclass=ABCMeta):
    Input = AddOrRemoveVideoInput

    @abstractmethod
    async def add_video(self, data: Input) -> None:
        pass


class RemoveVideo(metaclass=ABCMeta):
    Input = AddOrRemoveVideoInput

    @abstractmethod
    async def remove_video(self, data: Input) -> None:
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
