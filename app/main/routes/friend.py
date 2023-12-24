from app.schemas.friend import FriendsListOut, FriendInput
from app.schemas.common import MessageResponse, PATH_UUID
from app.main.dependencies import JwtBearer
from fastapi.routing import APIRouter
from app.main.config import PREFIX
from app.main.factories import (
    make_db_remove_friend,
    make_db_list_friends,
    make_db_add_friend
)
from typing import Annotated
from fastapi import Depends


router = APIRouter(prefix=f"{PREFIX}/friend", tags=['Friend'])


@router.get(
    "/list",
    status_code=200,
    summary="List Friends",
    response_description="All Friends",
    response_model=FriendsListOut
)
async def list_all_friends(uuid: Annotated[str, Depends(JwtBearer())]):
    db_list_friends = make_db_list_friends()
    friends = await db_list_friends.list_all(uuid)

    return FriendsListOut(message="Friends found", data=friends)


@router.patch(
    "/add/{friend_uuid}",
    status_code=200,
    summary="Add a Friend",
    response_description="Friend Added",
    response_model=MessageResponse
)
async def add_friend(
    uuid: Annotated[str, Depends(JwtBearer())],
    friend_uuid: PATH_UUID
):
    db_add_friend = make_db_add_friend()
    friend_input = FriendInput.make(uuid, friend_uuid)
    await db_add_friend.add_friend(friend_input)

    return MessageResponse(message="Friend added successfully")


@router.patch(
    "/remove/{friend_uuid}",
    status_code=200,
    summary="Remove a Friend",
    response_description="Friend Removed",
    response_model=MessageResponse
)
async def remove_friend(
    uuid: Annotated[str, Depends(JwtBearer())],
    friend_uuid: PATH_UUID
):
    db_add_friend = make_db_remove_friend()
    friend_input = FriendInput.make(uuid, friend_uuid)
    await db_add_friend.remove_friend(friend_input)

    return MessageResponse(message="Friend removed successfully")
