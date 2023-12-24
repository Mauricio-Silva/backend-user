from app.main.dependencies import JwtBearer, EmailApi, RequestBody
from app.schemas.common import MessageResponse
from fastapi.routing import APIRouter
from app.main.config import PREFIX
from fastapi import Body, Depends
from app.main.factories import (
    make_db_set_new_password,
    make_db_update_password,
    make_db_reset_password,
    make_db_validate_email,
    make_db_auth_login
)
from app.schemas.auth import (
    PasswordUpdate,
    SetNewPassword,
    PasswordReset,
    UserLogin,
    LoginOut
)
from typing import Annotated


router = APIRouter(prefix=f"{PREFIX}/auth", tags=['Auth'])


@router.post(
    "/login",
    status_code=200,
    summary="Login a Profile",
    response_description="Profile Logged",
    response_model=LoginOut,
    dependencies=[Depends(RequestBody())]
)
async def login(data: Annotated[UserLogin, Body()]):
    db_auth_login = make_db_auth_login()
    user = await db_auth_login.login(data)

    return LoginOut(message="Login successfully", data=user)


@router.put(
    "/update-password",
    status_code=200,
    summary="Update User Password",
    response_description="User Password Updated",
    response_model=MessageResponse,
    dependencies=[Depends(RequestBody())]
)
async def update_password(
    uuid: Annotated[str, Depends(JwtBearer())],
    data: Annotated[PasswordUpdate, Body()]
):
    data.uuid = uuid
    db_update_password = make_db_update_password()
    await db_update_password.update_password(data)

    return MessageResponse(message="User password successfully updated")


@router.post(
    "/reset-password",
    status_code=200,
    summary="Reset User Password",
    response_description="Resetting Password",
    response_model=MessageResponse,
    dependencies=[Depends(RequestBody()), Depends(EmailApi())]
)
async def reset_password(data: Annotated[PasswordReset, Body()]):
    db_reset_password = make_db_reset_password()
    await db_reset_password.reset_password(data)

    return MessageResponse(message="Email to reset password successfully sent")


@router.post(
    "/set-new-password",
    status_code=200,
    summary="Set New Password",
    response_description="Setting New Password",
    response_model=MessageResponse,
    dependencies=[Depends(RequestBody())]
)
async def set_new_password(
    uuid: Annotated[str, Depends(JwtBearer())],
    data: Annotated[SetNewPassword, Body()]
):
    data.uuid = uuid
    db_set_new_password = make_db_set_new_password()
    await db_set_new_password.set_new_password(data)

    return MessageResponse(message="New Password successfully setted")


@router.post(
    "/check-email",
    status_code=200,
    summary="Validate User Email",
    response_description="Validating Email",
    response_model=MessageResponse,
    dependencies=[Depends(EmailApi())]
)
async def validate_user_email(uuid: Annotated[str, Depends(JwtBearer())]):
    db_validate_email = make_db_validate_email()
    await db_validate_email.validate_email(uuid)

    return MessageResponse(message="Email successfully validated")
