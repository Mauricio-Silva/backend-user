from .database import MongoConnection
from app.data.protocols import ManagePhotoRepository
from app.main.exceptions import (
    Conflict,
    InternalError,
    NotFound
)
from app.schemas.photo import OperationType
from .projections import PHOTO_PROJECTION
from bson import ObjectId


class PhotoMongoRepository(ManagePhotoRepository):
    KEY = "photo"

    async def manage_photo(self, data: ManagePhotoRepository.Input) -> ManagePhotoRepository.Output:
        with MongoConnection() as collection:
            user = collection.find_one({"_id": ObjectId(data.user_uuid)}, PHOTO_PROJECTION)
            if user is None:
                raise NotFound("User")

            if data.photo_url is None or data.photo_url.strip() == "" or not len(data.photo_url):
                operation = OperationType.REMOVED

                if user[self.KEY] is not None:
                    update = (True, None)

                else:
                    raise Conflict("Photo already setted")

            elif user[self.KEY] is None:
                operation = OperationType.ADDED
                update = (True, data.photo_url)

            elif user[self.KEY] == data.photo_url:
                raise Conflict("Photo already setted")

            else:
                operation = OperationType.UPDATED
                update = (True, data.photo_url)

            if update[0]:
                manage_photo_update = {"$set": {self.KEY: update[1]}}
                result = collection.update_one({"_id": ObjectId(data.user_uuid)}, manage_photo_update)

                if result.matched_count == 0:
                    raise NotFound("User")
                if result.matched_count == 1 and result.modified_count == 0:
                    prefix = operation.value.removesuffix("ed")
                    raise InternalError(f"Error in {prefix}ing video")

            return operation
