from app.data.usecases.admin import (
    DbResendEmail,
    DbGetToken,
    DbSearchAccounts
)
from app.infra.mongo import UserMongoRepository, AccountMongoRepository
from app.main.config import EXPIRE_RESET_PASSWORD_TIME
from app.infra.auth import JwtRepository
from app.infra.gateway import EmailService
from fastapi import Request


def make_db_resend_email(request: Request) -> DbResendEmail:
    user_mongo_repository = UserMongoRepository()
    jwt_repository = JwtRepository(EXPIRE_RESET_PASSWORD_TIME)
    email_service = EmailService()
    return DbResendEmail(
        request,
        user_mongo_repository,
        jwt_repository,
        email_service
    )


def make_db_get_token(request: Request) -> DbGetToken:
    user_mongo_repository = UserMongoRepository()
    jwt_repository = JwtRepository()
    return DbGetToken(
        request,
        user_mongo_repository,
        jwt_repository
    )


def make_db_search_accounts():
    admin_mongo_repository = AccountMongoRepository()
    return DbSearchAccounts(admin_mongo_repository)
