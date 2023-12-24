from app.data.usecases.admin import (
    DbResendEmail,
    DbGetToken,
    DbSearchAccounts
)
from app.infra.mongo.repositories import UserMongoRepository, AccountMongoRepository
from app.main.config import EXPIRE_RESET_PASSWORD_TIME
from app.infra.auth import JwtRepository
from app.infra.gateway import EmailService


def make_db_resend_email() -> DbResendEmail:
    user_mongo_repository = UserMongoRepository()
    jwt_repository = JwtRepository(EXPIRE_RESET_PASSWORD_TIME)
    email_service = EmailService()
    return DbResendEmail(
        user_mongo_repository,
        jwt_repository,
        email_service
    )


def make_db_get_token() -> DbGetToken:
    user_mongo_repository = UserMongoRepository()
    jwt_repository = JwtRepository()
    return DbGetToken(
        user_mongo_repository,
        jwt_repository
    )


def make_db_search_accounts():
    admin_mongo_repository = AccountMongoRepository()
    return DbSearchAccounts(admin_mongo_repository)
