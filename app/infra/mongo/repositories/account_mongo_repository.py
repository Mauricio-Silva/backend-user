from app.infra.mongo.projections import PASSWORD_PROJECTION, USER_MODEL_OUT_PROJECTION
from app.infra.mongo.database import MongoConnection
from app.data.protocols import (
    GetPasswordByUuidRepository,
    UpdatePasswordRepository,
    SetNewPasswordRepository,
    SearchAccountsRepository,
    ValidateAccountRepository
)
from app.main.exceptions import InternalError, NotFound
from app.domain.models import UserModelOut
from app.usecase import AccountSearch
from datetime import datetime
from bson import ObjectId


class AccountMongoRepository(
    GetPasswordByUuidRepository,
    UpdatePasswordRepository,
    SetNewPasswordRepository,
    ValidateAccountRepository
):
    KEY = "password"

    async def get_by_id(self, uuid: str) -> str:
        with MongoConnection() as collection:
            result = collection.find_one({"_id": ObjectId(uuid)}, PASSWORD_PROJECTION)
            return None if result is None else result[self.KEY]

    async def update_password(self, data: UpdatePasswordRepository.Input) -> None:
        with MongoConnection() as collection:
            password_update = {"$set": {self.KEY: data.new_password}}
            result = collection.update_one({"_id": ObjectId(data.uuid)}, password_update)
            if result.matched_count == 0:
                raise NotFound("User")
            if result.matched_count == 1 and result.modified_count == 0:
                raise InternalError("Error in updating password")

    async def set_new_password(self, data: SetNewPasswordRepository.Input) -> None:
        with MongoConnection() as collection:
            password_update = {"$set": {self.KEY: data.password}}
            result = collection.update_one({"_id": ObjectId(data.uuid)}, password_update)
            if result.matched_count == 0:
                raise NotFound("User")
            if result.matched_count == 1 and result.modified_count == 0:
                raise InternalError("Error in updating password")

    async def search(self, data: str) -> SearchAccountsRepository.Output:
        with MongoConnection() as collection:
            if not collection.count_documents({}):
                return None
            user_search = AccountSearch(collection, data, 0.7)
            results = user_search.search()
            return None if not results else results

    async def validate(self, uuid: str) -> ValidateAccountRepository.Output:
        update_account = {"is_enabled": True, "verified_at": datetime.now()}
        with MongoConnection() as collection:
            result = collection.update_one({"_id": ObjectId(uuid)}, {"$set": update_account})
            if result.matched_count == 0:
                raise NotFound("User")
            if result.matched_count == 1 and result.modified_count == 0:
                raise InternalError("Error in activating user")
            result = collection.find_one({"_id": ObjectId(uuid)}, USER_MODEL_OUT_PROJECTION)
            return None if not result else UserModelOut(**result)
