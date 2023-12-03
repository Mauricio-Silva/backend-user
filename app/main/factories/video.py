from app.data.usecases.video import (
    DbListVideos,
    DbListMyVideos,
    DbListFriendsVideos
)
from app.infra.mongo.repositories import VideoMongoRepository


def make_db_list_videos() -> DbListVideos:
    video_mongo_repository = VideoMongoRepository()
    return DbListVideos(video_mongo_repository)


def make_db_list_my_videos() -> DbListMyVideos:
    video_mongo_repository = VideoMongoRepository()
    return DbListMyVideos(video_mongo_repository)


def make_db_list_friends_videos() -> DbListFriendsVideos:
    video_mongo_repository = VideoMongoRepository()
    return DbListFriendsVideos(video_mongo_repository)
