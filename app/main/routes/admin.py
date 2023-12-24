from app.main.dependencies import AccessKey, EmailApi, RequestBody
from app.schemas.common import MessageResponse, ACCOUNT_SEARCH
from app.utils.serializations import exceptions_responses
from app.main.exceptions import RequiredQueryParam
from fastapi.routing import APIRouter
from app.main.config import PREFIX
from fastapi import Body, Depends
from app.main.factories import (
    make_db_search_accounts,
    make_db_resend_email,
    make_db_get_token
)
from app.schemas.admin import (
    AccountLogin,
    AccountsOut,
    EmailResend,
    LoginOut
)
from typing import Annotated


router = APIRouter(prefix=f"{PREFIX}/admin", tags=['Admin'])


@router.post(
    "/resend-email",
    status_code=200,
    summary="Resend Email",
    response_description="Resending Email",
    response_model=MessageResponse,
    dependencies=[
        Depends(AccessKey()),
        Depends(RequestBody()),
        Depends(EmailApi())
    ],
    description=exceptions_responses(422, 404, 409, 500, 424),
)
async def resend_email(data: Annotated[EmailResend, Body()]):
    db_resend_email = make_db_resend_email()
    await db_resend_email.resend_email(data)

    return MessageResponse(message="Email resended successfully")


@router.post(
    "/get-token",
    status_code=200,
    summary="Get Login Token",
    response_description="Profile Logged",
    response_model=LoginOut,
    dependencies=[Depends(AccessKey()), Depends(RequestBody())]
)
async def get_token(data: Annotated[AccountLogin, Body()]):
    db_get_token = make_db_get_token()
    user = await db_get_token.get_token(data)

    return LoginOut(message="Login successfully", data=user)


@router.get(
    "",
    status_code=200,
    summary="Search Account by Email",
    response_description="Account(s) found",
    response_model=AccountsOut,
    dependencies=[Depends(AccessKey())]
)
async def search_account(q: ACCOUNT_SEARCH):
    if not q:
        raise RequiredQueryParam("Search")

    db_search_accounts = make_db_search_accounts()
    accounts = await db_search_accounts.search(q)

    return AccountsOut(message="Accounts found", data=accounts)
