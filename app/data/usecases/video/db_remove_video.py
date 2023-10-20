from app.domain.usecases import RemoveVideo
from app.data.protocols import RemoveVideoRepository


class DbRemoveVideo(RemoveVideo):
    def __init__(
        self,
        remove_video_repository: RemoveVideoRepository
    ) -> None:
        self.__remove_video_repository = remove_video_repository

    async def remove_video(self, data: RemoveVideo.Input) -> None:
        await self.__remove_video_repository.remove_video(data)
