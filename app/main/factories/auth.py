from app.data.usecases.auth import (
    AuthLogin,
    DbUpdatePassword
)
from app.infra.mongo import UserMongoRepository, AccountMongoRepository
from app.infra.auth import JwtRepository
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
