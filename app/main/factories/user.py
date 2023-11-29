from app.data.usecases.user import (
    DbListUsers,
    DbPersonalProfile,
    DbGetUser,
    DbSearchUser,
    DbCreateUser,
    DbUpdateUser,
    DbDeleteUser,
    DbEnableUser,
    DbDisableUser
)
from app.infra.mongo.repositories import UserMongoRepository
from app.infra.auth import JwtRepository


def make_db_list_users() -> DbListUsers:
    user_mongo_repository = UserMongoRepository()
    return DbListUsers(user_mongo_repository)


def make_db_personal_profile() -> DbPersonalProfile:
    user_mongo_repository = UserMongoRepository()
    return DbPersonalProfile(user_mongo_repository)


def make_db_get_user() -> DbGetUser:
    user_mongo_repository = UserMongoRepository()
    return DbGetUser(user_mongo_repository)


def make_db_search_user() -> DbSearchUser:
    user_mongo_repository = UserMongoRepository()
    return DbSearchUser(user_mongo_repository)


def make_db_create_user() -> DbCreateUser:
    jwt_repository = JwtRepository()
    user_mongo_repository = UserMongoRepository()
    return DbCreateUser(
        jwt_repository,
        user_mongo_repository,
        user_mongo_repository
    )


def make_db_update_user() -> DbUpdateUser:
    user_mongo_repository = UserMongoRepository()
    return DbUpdateUser(user_mongo_repository)


def make_db_delete_user() -> DbDeleteUser:
    user_mongo_repository = UserMongoRepository()
    return DbDeleteUser(user_mongo_repository)


def make_db_disable_user() -> DbDisableUser:
    user_mongo_repository = UserMongoRepository()
    return DbDisableUser(user_mongo_repository)


def make_db_enable_user() -> DbEnableUser:
    user_mongo_repository = UserMongoRepository()
    return DbEnableUser(user_mongo_repository)
