from app.domain.usecases import ListFriendsVideos
from app.data.protocols import ListFriendsVideosRepository


class DbListFriendsVideos(ListFriendsVideos):
    def __init__(
        self,
        list_friends_videos_repository: ListFriendsVideosRepository
    ) -> None:
        self.__list_friends_videos_repository = list_friends_videos_repository

    async def list_friends_videos(self, uuid: str) -> ListFriendsVideos.Output:
        return await self.__list_friends_videos_repository.list_friends_videos(uuid)
