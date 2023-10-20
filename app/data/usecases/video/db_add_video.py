from app.domain.usecases import AddVideo
from app.data.protocols import AddVideoRepository


class DbAddVideo(AddVideo):
    def __init__(
        self,
        add_video_repository: AddVideoRepository
    ) -> None:
        self.__add_video_repository = add_video_repository

    async def add_video(self, data: AddVideo.Input) -> None:
        await self.__add_video_repository.add_video(data)
