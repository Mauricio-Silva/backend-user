from fastapi.routing import APIRouter
from typing import Annotated
from fastapi import Depends, Body
from app.main.factories import make_db_manage_photo
from app.schemas.common import MessageResponse
from app.schemas.photo import PhotoInput
from app.main.exceptions import (
    RequiredRequestBody,
    InvalidUuid
)
from app.infra.auth import JwtBearer
from app.main.config import PREFIX
from bson import ObjectId


router = APIRouter(prefix=f"{PREFIX}/photo", tags=['Photo'])


@router.patch(
    "/",
    status_code=200,
    summary="Manage Photo",
    response_description="Photo managed",
    response_model=MessageResponse
)
async def manage_photo(
    uuid: Annotated[str, Depends(JwtBearer())],
    data: Annotated[PhotoInput, Body()]
):
    if not data:
        raise RequiredRequestBody()

    if not ObjectId.is_valid(uuid):
        raise InvalidUuid("user")

    data.user_uuid = uuid
    db_manage_photo = make_db_manage_photo()
    operation = await db_manage_photo.manage_photo(data)

    return MessageResponse(message=f"Photo {operation.value} successfully")
