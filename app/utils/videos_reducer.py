from app.domain.models import VideoModelOut
from functools import reduce


class VideosListReducer:
    KEY = "videos"

    @classmethod
    def __sorter(cls, data: VideoModelOut):
        return data.upload_at

    @classmethod
    def __list_all_reducer(cls, result: list, data: dict):
        if len(data):
            result.append(VideoModelOut(**data))
        return result

    @classmethod
    def list_all(cls, results: list[dict | None]) -> list[VideoModelOut]:
        videos = reduce(cls.__list_all_reducer, results, [])
        return sorted(videos, key=cls.__sorter, reverse=True)

    @classmethod
    def __mapper(cls, data: dict):
        return VideoModelOut(**data)

    @classmethod
    def __list_friends_videos_reducer(cls, result: list, data: dict):
        if len(data[cls.KEY]):
            videos = map(cls.__mapper, data[cls.KEY])
            result.extend(videos)
        return result

    @classmethod
    def list_friends_videos(cls, results: list[dict | None]) -> list[VideoModelOut]:
        videos = reduce(cls.__list_friends_videos_reducer, results, [])
        return sorted(videos, key=cls.__sorter, reverse=True)
