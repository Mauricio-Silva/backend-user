from fastapi.routing import APIRouter
from typing import Annotated
from fastapi import Request, Body, Depends
from app.main.factories import (
    make_db_resend_email,
    make_db_get_token,
    make_db_search_accounts
)
from app.schemas.common import MessageResponse, ACCOUNT_SEARCH
from app.schemas.admin import (
    AccountsOut,
    EmailResend,
    AccountLogin,
    LoginOut
)
from app.main.exceptions import RequiredRequestBody, RequiredQueryParam
from app.utils.serializations import exceptions_responses
from app.infra.auth import AccessKey
from app.infra.gateway import EmailApi
from app.main.config import PREFIX


router = APIRouter(prefix=f"{PREFIX}/admin", tags=['Admin'])


@router.post(
    "/resend-email",
    status_code=200,
    summary="Resend Email",
    response_description="Resending Email",
    response_model=MessageResponse,
    dependencies=[Depends(AccessKey()), Depends(EmailApi())],
    description=exceptions_responses(422, 404, 409, 500, 424),
)
async def resend_email(data: Annotated[EmailResend, Body()]):
    if not data:
        raise RequiredRequestBody()

    db_resend_email = make_db_resend_email()
    await db_resend_email.resend_email(data)

    return MessageResponse(message="Email resended successfully")


@router.post(
    "/get-token",
    status_code=200,
    summary="Get Login Token",
    response_description="Profile Logged",
    response_model=LoginOut,
    dependencies=[Depends(AccessKey())]
)
async def get_token(data: Annotated[AccountLogin, Body()]):
    if not data:
        raise RequiredRequestBody()

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
