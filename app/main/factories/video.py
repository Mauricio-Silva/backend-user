from app.data.usecases.video import (
    DbListVideos,
    DbListMyVideos,
    DbListFriendsVideos,
    DbAddVideo,
    DbRemoveVideo,
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


def make_db_add_video() -> DbAddVideo:
    video_mongo_repository = VideoMongoRepository()
    return DbAddVideo(video_mongo_repository)


def make_db_remove_video() -> DbRemoveVideo:
    video_mongo_repository = VideoMongoRepository()
    return DbRemoveVideo(video_mongo_repository)
