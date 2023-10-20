from app.domain.usecases import ListVideos
from app.data.protocols import ListVideosRepository


class DbListVideos(ListVideos):
    def __init__(
        self,
        list_videos_repository: ListVideosRepository
    ) -> None:
        self.__list_videos_repository = list_videos_repository

    async def list_all(self) -> ListVideos.Output:
        return await self.__list_videos_repository.list_all()
