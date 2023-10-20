from app.main.config import MongoConnection
from app.data.protocols import (
    ListUsersRepository,
    PersonalProfileRepository,
    GetUserByUuidRepository,
    SearchUserRepository,
    GetUserByUniqueRepository,
    CreateUserRepository,
    UpdateUserRepository,
    DeleteUserRepository,
    DisableUserRepository,
    EnableUserRepository
)
from app.models import CreateUserDocument, UpdateUserDocument
from app.usecase import UserSearch, UserGetUnique
from app.main.exceptions import NotFound, InternalError
from .projections import (
    USER_MODEL_OUT_PROJECTION,
    PROFILE_MODEL_OUT_PROJECTION
)
from app.domain.models import UserModelOut, ProfileModelOut
from bson import ObjectId


class UserMongoRepository(
    ListUsersRepository,
    PersonalProfileRepository,
    GetUserByUuidRepository,
    SearchUserRepository,
    GetUserByUniqueRepository,
    CreateUserRepository,
    UpdateUserRepository,
    DeleteUserRepository,
    DisableUserRepository,
    EnableUserRepository
):
    async def list_all(self) -> ListUsersRepository.Output:
        with MongoConnection() as collection:
            if not collection.count_documents({}):
                return None
            results = collection.find({}, USER_MODEL_OUT_PROJECTION)
            return [UserModelOut(**user) for user in results]

    async def get_personal_profile(self, uuid: str) -> PersonalProfileRepository.Output:
        with MongoConnection() as collection:
            result = collection.find_one({"_id": ObjectId(uuid)}, PROFILE_MODEL_OUT_PROJECTION)
            return None if result is None else ProfileModelOut(**result)

    async def get_by_id(self, uuid: str) -> GetUserByUuidRepository.Output:
        with MongoConnection() as collection:
            result = collection.find_one({"_id": ObjectId(uuid)}, USER_MODEL_OUT_PROJECTION)
            return None if result is None else UserModelOut(**result)

    async def search(self, data: str) -> SearchUserRepository.Output:
        with MongoConnection() as collection:
            if not collection.count_documents({}):
                return None
            user_search = UserSearch(data, 0.7)
            results = user_search.search(collection.find({}, USER_MODEL_OUT_PROJECTION))
            return None if not results else results

    async def check_unique(self, data: GetUserByUniqueRepository.Input) -> None:
        with MongoConnection() as collection:
            if not collection.count_documents({}):
                return None
            user_get_unique = UserGetUnique(collection)
            user_get_unique.check_unique(data)

    async def get_by_unique(self, username_or_email: str) -> GetUserByUniqueRepository.Output:
        with MongoConnection() as collection:
            if not collection.count_documents({}):
                raise NotFound("User not found. Empty database")
            user_get_unique = UserGetUnique(collection)
            result = user_get_unique.get_by_unique(username_or_email)
            return None if not result else result

    async def create(self, data: CreateUserRepository.Input) -> CreateUserRepository.Output:
        user = CreateUserDocument(**data.model_dump(exclude_none=True))
        with MongoConnection() as collection:
            new_user = collection.insert_one(user.model_dump())
            result = collection.find_one({"_id": ObjectId(new_user.inserted_id)}, USER_MODEL_OUT_PROJECTION)
            return None if not result else UserModelOut(**result)

    async def update(self, data: UpdateUserRepository.Input) -> UpdateUserRepository.Output:
        update_user_document = UpdateUserDocument(**data.model_dump())
        update_user = update_user_document.model_dump(exclude_none=True)
        with MongoConnection() as collection:
            result = collection.update_one({"_id": ObjectId(data.uuid)}, {"$set": update_user})
            if result.modified_count == 0 and result.matched_count == 1:
                raise InternalError("Error in updating user")
            result = collection.find_one({"_id": ObjectId(data.uuid)}, USER_MODEL_OUT_PROJECTION)
            return None if not result else UserModelOut(**result)

    async def delete(self, uuid: str) -> None:
        with MongoConnection() as collection:
            result = collection.delete_one({"_id": ObjectId(uuid)})
            if result.deleted_count != 1:
                raise InternalError("Error in deleting user")

    async def disable(self, uuid: str) -> DisableUserRepository.Output:
        with MongoConnection() as collection:
            result = collection.update_one({"_id": ObjectId(uuid)}, {"$set": {"is_enabled": False}})
            if result.modified_count == 0 and result.matched_count == 1:
                raise InternalError("Error in deactivating user")
            result = collection.find_one({"_id": ObjectId(uuid)}, USER_MODEL_OUT_PROJECTION)
            return None if not result else UserModelOut(**result)

    async def enable(self, uuid: str) -> EnableUserRepository.Output:
        with MongoConnection() as collection:
            result = collection.update_one({"_id": ObjectId(uuid)}, {"$set": {"is_enabled": True}})
            if result.modified_count == 0 and result.matched_count == 1:
                raise InternalError("Error in activating user")
            result = collection.find_one({"_id": ObjectId(uuid)}, USER_MODEL_OUT_PROJECTION)
            return None if not result else UserModelOut(**result)
