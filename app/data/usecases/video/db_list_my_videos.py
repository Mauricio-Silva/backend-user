from app.domain.usecases import ListMyVideos
from app.data.protocols import ListMyVideosRepository


class DbListMyVideos(ListMyVideos):
    def __init__(
        self,
        list_my_videos_repository: ListMyVideosRepository
    ) -> None:
        self.__list_my_videos_repository = list_my_videos_repository

    async def list_my_videos(self, uuid: str) -> ListMyVideos.Output:
        return await self.__list_my_videos_repository.list_my_videos(uuid)
