from app.main.config import MongoConnection
from app.data.protocols import (
    GetPasswordByUuidRepository,
    UpdatePasswordRepository,
)
from app.main.exceptions import InternalError
from .projections import PASSWORD_PROJECTION
from bson import ObjectId


class AccountMongoRepository(
    GetPasswordByUuidRepository,
    UpdatePasswordRepository,
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
            if result.modified_count == 0 and result.matched_count == 1:
                raise InternalError("Error in updating password")
