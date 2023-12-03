from fastapi.routing import APIRouter
from typing import Annotated
from fastapi import Depends
from app.main.factories import (
    make_db_list_videos,
    make_db_list_my_videos,
    make_db_list_friends_videos
)
from app.schemas.video import VideosListOut
from app.infra.auth import JwtBearer
from app.main.config import PREFIX


router = APIRouter(prefix=f"{PREFIX}/video", tags=['Video'])


@router.get(
    "/list",
    status_code=200,
    summary="List Videos",
    response_description="All Videos",
    response_model=VideosListOut,
    dependencies=[Depends(JwtBearer())]
)
async def list_all_videos():
    db_list_videos = make_db_list_videos()
    videos = await db_list_videos.list_all()

    return VideosListOut(message="Videos found", data=videos)


@router.get(
    "/list/me",
    status_code=200,
    summary="List User Videos",
    response_description="User Videos",
    response_model=VideosListOut
)
async def list_my_videos(uuid: Annotated[str, Depends(JwtBearer())]):
    db_list_my_videos = make_db_list_my_videos()
    videos = await db_list_my_videos.list_my_videos(uuid)

    return VideosListOut(message="My videos found", data=videos)


@router.get(
    "/list/friends",
    status_code=200,
    summary="List Friends Videos",
    response_description="Friends Videos",
    response_model=VideosListOut
)
async def list_friends_videos(uuid: Annotated[str, Depends(JwtBearer())]):
    db_list_friends_videos = make_db_list_friends_videos()
    videos = await db_list_friends_videos.list_friends_videos(uuid)

    return VideosListOut(message="Friends videos found", data=videos)
