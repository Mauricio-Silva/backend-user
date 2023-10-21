from fastapi.routing import APIRouter
from typing import Annotated
from fastapi import Body, Depends
from app.main.factories import (
    make_db_list_users,
    make_db_personal_profile,
    make_db_get_user,
    make_db_search_user,
    make_db_create_user,
    make_db_update_user,
    make_db_delete_user,
    make_db_disable_user,
    make_db_enable_user
)
from app.schemas.user import (
    UserOut,
    UsersOut,
    ProfileOut,
    UserCreate,
    UserUpdate
)
from app.schemas.common import PATH_UUID, QUERY_SEARCH, MessageResponse
from app.main.exceptions import (
    RequiredQueryParam,
    InvalidUuid,
    RequiredRequestBody
)
from app.infra.auth import JwtBearer
from app.main.config import PREFIX
from bson import ObjectId


router = APIRouter(prefix=f"{PREFIX}/user", tags=['Profile'])


@router.get(
    "/list",
    status_code=200,
    summary="List Profiles",
    response_description="All Profiles",
    response_model=UsersOut
)
async def list_all_profiles():
    db_list_users = make_db_list_users()
    users = await db_list_users.list_all()

    return UsersOut(message="Users found", data=users)


@router.get(
    "/my-account",
    status_code=200,
    summary="Get Personal Profile",
    response_description="Personal Profile",
    response_model=ProfileOut
)
async def get_personal_profile(uuid: Annotated[str, Depends(JwtBearer())]):
    if not ObjectId.is_valid(uuid):
        raise InvalidUuid("user")

    db_personal_profile = make_db_personal_profile()
    profile = await db_personal_profile.get_personal_profile(uuid)

    return ProfileOut(message="Personal profile", data=profile)


@router.get(
    "/{uuid}",
    status_code=200,
    summary="Get Profile by ID",
    response_description="Profile found",
    response_model=UserOut
)
async def get_profile_by_id(uuid: PATH_UUID):
    if not ObjectId.is_valid(uuid):
        raise InvalidUuid("user")

    db_get_user = make_db_get_user()
    user = await db_get_user.get_by_id(uuid)

    return UserOut(message="User found", data=user)


@router.get(
    "/",
    status_code=200,
    summary="Search Profile by Name or Username",
    response_description="Profile(s) found",
    response_model=UsersOut
)
async def search_profile(q: QUERY_SEARCH):
    if not q:
        raise RequiredQueryParam("Search")

    db_search_user = make_db_search_user()
    users = await db_search_user.search(q)

    return UsersOut(message="Users found", data=users)


@router.post(
    "/",
    status_code=201,
    summary="Create a new Profile",
    response_description="Profile Created",
    response_model=UserOut
)
async def create_profile(data: Annotated[UserCreate, Body()]):
    if not data:
        raise RequiredRequestBody()

    db_create_user = make_db_create_user()
    user = await db_create_user.create(data)

    return UserOut(message="User created", data=user)


@router.put(
    "/",
    status_code=200,
    summary="Update a Profile",
    response_description="Profile Updated",
    response_model=UserOut
)
async def update_profile(
    uuid: Annotated[str, Depends(JwtBearer())],
    data: Annotated[UserUpdate, Body()]
):
    if not data:
        raise RequiredRequestBody()

    if not ObjectId.is_valid(uuid):
        raise InvalidUuid("user")

    data.uuid = uuid
    db_update_user = make_db_update_user()
    user = await db_update_user.update(data)

    return UserOut(message="User updated", data=user)


@router.delete(
    "/",
    status_code=200,
    summary="Delete a Profile",
    response_description="Profile Deleted",
    response_model=MessageResponse
)
async def delete_profile(uuid: Annotated[str, Depends(JwtBearer())]):
    if not ObjectId.is_valid(uuid):
        raise InvalidUuid("user")

    db_delete_user = make_db_delete_user()
    await db_delete_user.delete(uuid)

    return MessageResponse(message="User was successfully deleted")


@router.patch(
    "/disable",
    status_code=200,
    summary="Disable a Profile",
    response_description="Profile Disabled",
    response_model=UserOut
)
async def disable_profile(uuid: Annotated[str, Depends(JwtBearer())]):
    if not ObjectId.is_valid(uuid):
        raise InvalidUuid("user")

    db_disable_user = make_db_disable_user()
    user = await db_disable_user.disable(uuid)

    return UserOut(message="User disabled", data=user)


@router.patch(
    "/enable",
    status_code=200,
    summary="Enable a Profile",
    response_description="Profile Enabled",
    response_model=UserOut
)
async def enable_profile(uuid: Annotated[str, Depends(JwtBearer())]):
    if not ObjectId.is_valid(uuid):
        raise InvalidUuid("user")

    db_enable_user = make_db_enable_user()
    user = await db_enable_user.enable(uuid)

    return UserOut(message="User enabled", data=user)
