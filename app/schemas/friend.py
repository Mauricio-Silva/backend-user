from pydantic import BaseModel, Field
from app.schemas.common import BaseResponse
from app.domain.models import UserModelOut


class FriendsListOut(BaseResponse):
    data: list[UserModelOut]


class FriendInput(BaseModel):
    user_uuid: str = Field(..., min_length=24, max_length=24)
    friend_uuid: str = Field(..., min_length=24, max_length=24)

    @staticmethod
    def make(user_uuid: str, friend_uuid: str):
        return FriendInput(user_uuid=user_uuid, friend_uuid=friend_uuid)
