from pydantic import BaseModel, Field
from app.schemas.common import BaseResponse
from app.domain.models import UserModelOut
from app.utils.custom_types import UUID_VALIDATOR


class FriendsListOut(BaseResponse):
    data: list[UserModelOut]


class FriendInput(BaseModel):
    user_uuid: UUID_VALIDATOR = Field(..., min_length=24, max_length=24)
    friend_uuid: UUID_VALIDATOR = Field(..., min_length=24, max_length=24)

    @staticmethod
    def make(user_uuid: str, friend_uuid: str):
        return FriendInput(user_uuid=user_uuid, friend_uuid=friend_uuid)
