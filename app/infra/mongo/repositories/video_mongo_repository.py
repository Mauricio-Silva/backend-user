from app.infra.mongo.database import MongoConnection
from app.data.protocols import (
    ListVideosRepository,
    AddVideoRepository,
    RemoveVideoRepository
)
from app.main.exceptions import (
    Conflict,
    InternalError,
    NotFound
)
from app.infra.mongo.projections import (
    VIDEOS_PROJECTION,
    FRIENDS_PROJECTION
)
from app.domain.models import VideoModelOut
from app.models import AddVideoDocument
from app.utils.videos_reducer import VideosListReducer
from bson import ObjectId


class VideoMongoRepository(
    ListVideosRepository,
    AddVideoRepository,
    RemoveVideoRepository
):
    KEY = "videos"
    FKEY = "friends"

    async def list_all(self) -> ListVideosRepository.Output:
        with MongoConnection() as collection:
            if not collection.count_documents({}):
                return None
            results = collection.distinct(self.KEY)
            return VideosListReducer.list_all(results)

    async def add_video(self, data: AddVideoRepository.Input) -> None:
        with MongoConnection() as collection:
            user = collection.find_one({"_id": ObjectId(data.user_uuid)}, VIDEOS_PROJECTION)
            if user is None:
                raise NotFound("User")

            videos = [] if user[self.KEY] is None else list(user[self.KEY])
            urls = [video["url"] for video in videos]
            if data.video_url in urls:
                raise Conflict("Video already exists")

            video = AddVideoDocument(url=data.video_url, uuid=data.video_uuid)
            videos.append(video.model_dump())
            add_video_update = {"$set": {self.KEY: videos}}

            result = collection.update_one({"_id": ObjectId(data.user_uuid)}, add_video_update)
            if result.matched_count == 0:
                raise NotFound("User")
            if result.matched_count == 1 and result.modified_count == 0:
                raise InternalError("Error in adding video")

    async def remove_video(self, data: RemoveVideoRepository.Input) -> None:
        with MongoConnection() as collection:
            user = collection.find_one({"_id": ObjectId(data.user_uuid)}, VIDEOS_PROJECTION)
            if user is None or not user[self.KEY]:
                return NotFound("User")

            videos = list(user[self.KEY])
            urls = [video["url"] for video in videos]
            if data.video_url not in urls:
                raise NotFound("Video")

            videos.pop(urls.index(data.video_url))
            remove_video_update = {"$set": {self.KEY: videos}}

            result = collection.update_one({"_id": ObjectId(data.user_uuid)}, remove_video_update)
            if result.matched_count == 0:
                raise NotFound("User")
            if result.matched_count == 1 and result.modified_count == 0:
                raise InternalError("Error in removing video")

    async def list_my_videos(self, uuid: str) -> ListVideosRepository.Output:
        with MongoConnection() as collection:
            result = collection.find_one({"_id": ObjectId(uuid)}, VIDEOS_PROJECTION)
            if not result or not result[self.KEY]:
                return None
            return [VideoModelOut(**video) for video in result[self.KEY]]

    async def list_friends_videos(self, uuid: str) -> ListVideosRepository.Output:
        with MongoConnection() as collection:
            result = collection.find_one({"_id": ObjectId(uuid)}, FRIENDS_PROJECTION)
            if not result or not result[self.FKEY]:
                return None

            uuids_list = [ObjectId(uuid) for uuid in result[self.FKEY]]
            results = collection.find({"_id": {"$in": uuids_list}}, VIDEOS_PROJECTION)
            return VideosListReducer.list_friends_videos(results)
