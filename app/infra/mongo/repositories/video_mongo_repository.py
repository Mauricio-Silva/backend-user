from app.infra.mongo.database import MongoConnection
from app.data.protocols import ListVideosRepository
from app.infra.mongo.projections import (
    VIDEOS_PROJECTION,
    FRIENDS_PROJECTION
)
from app.domain.models import VideoModelOut
from app.utils.videos_reducer import VideosListReducer
from bson import ObjectId


class VideoMongoRepository(ListVideosRepository):
    KEY = "videos"
    FKEY = "friends"

    async def list_all(self) -> ListVideosRepository.Output:
        with MongoConnection() as collection:
            if not collection.count_documents({}):
                return None
            results = collection.distinct(self.KEY)
            return VideosListReducer.list_all(results)

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
