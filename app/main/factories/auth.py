from app.data.usecases.auth import (
    AuthLogin,
    DbUpdatePassword,
    DbResetPassword,
    DbSetNewPassword,
    DbCheckUserEmail,
    DbValidateUserEmail
)
from app.main.config import EXPIRE_RESET_PASSWORD_TIME, EXPIRE_CHECK_ACCOUNT_TIME
from app.infra.mongo import UserMongoRepository, AccountMongoRepository
from app.infra.auth import JwtRepository
from app.infra.gateway import EmailService
from fastapi import Request


def make_db_auth_login(request: Request) -> AuthLogin:
    user_mongo_repository = UserMongoRepository()
    jwt_repository = JwtRepository()

    return AuthLogin(
        request,
        user_mongo_repository,
        jwt_repository,
        jwt_repository
    )


def make_db_update_password() -> DbUpdatePassword:
    jwt_repository = JwtRepository()
    account_mongo_repository = AccountMongoRepository()

    return DbUpdatePassword(
        account_mongo_repository,
        jwt_repository,
        jwt_repository,
        account_mongo_repository
    )


def make_db_reset_password(request: Request) -> DbResetPassword:
    user_mongo_repository = UserMongoRepository()
    jwt_repository = JwtRepository(EXPIRE_RESET_PASSWORD_TIME)
    email_service = EmailService()
    return DbResetPassword(
        request,
        user_mongo_repository,
        jwt_repository,
        email_service
    )


def make_db_set_new_password() -> DbSetNewPassword:
    jwt_repository = JwtRepository()
    account_mongo_repository = AccountMongoRepository()
    return DbSetNewPassword(
        jwt_repository,
        account_mongo_repository
    )


def make_db_check_email(request: Request) -> DbCheckUserEmail:
    jwt_repository = JwtRepository(EXPIRE_CHECK_ACCOUNT_TIME)
    email_service = EmailService()
    return DbCheckUserEmail(
        request,
        jwt_repository,
        email_service
    )


def make_db_validate_email() -> DbValidateUserEmail:
    account_mongo_repository = AccountMongoRepository()
    return DbValidateUserEmail(account_mongo_repository)
