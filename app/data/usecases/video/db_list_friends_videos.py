from app.domain.usecases import ListFriendsVideos
from app.data.protocols import ListFriendsVideosRepository
from app.main.exceptions import NotFound


class DbListFriendsVideos(ListFriendsVideos):
    def __init__(
        self,
        list_friends_videos_repository: ListFriendsVideosRepository
    ) -> None:
        self.__list_friends_videos_repository = list_friends_videos_repository

    async def list_friends_videos(self, uuid: str) -> ListFriendsVideos.Output:
        videos = await self.__list_friends_videos_repository.list_friends_videos(uuid)

        if not videos:
            raise NotFound("Videos")

        return videos
