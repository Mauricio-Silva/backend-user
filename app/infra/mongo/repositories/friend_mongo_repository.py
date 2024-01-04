from app.infra.mongo.projections import USER_MODEL_OUT_PROJECTION, FRIENDS_PROJECTION
from app.infra.mongo.database import MongoConnection
from app.data.protocols import (
    ListFriendsRepository,
    AddFriendRepository,
    RemoveFriendRepository
)
from app.main.exceptions import (
    Conflict,
    InternalError,
    NotFound
)
from app.domain.models import UserModelOut
from bson import ObjectId


class FriendMongoRepository(
    ListFriendsRepository,
    AddFriendRepository,
    RemoveFriendRepository
):
    KEY = "friends"

    async def list_all(self, uuid: str) -> ListFriendsRepository.Output:
        with MongoConnection() as collection:
            result = collection.find_one({"_id": ObjectId(uuid)}, FRIENDS_PROJECTION)
            if not result or not result[self.KEY]:
                return None
            uuids_list = [ObjectId(uuid) for uuid in result[self.KEY]]
            results = collection.find({"_id": {"$in": uuids_list}}, USER_MODEL_OUT_PROJECTION)
            return [UserModelOut(**user) for user in results]

    async def add_friend(self, data: AddFriendRepository.Input) -> None:
        with MongoConnection() as collection:
            user = collection.find_one({"_id": ObjectId(data.user_uuid)}, FRIENDS_PROJECTION)
            if user is None:
                return None

            if data.friend_uuid in user[self.KEY]:
                raise Conflict("Friend already exists")

            add_friend_update = {"$push": {self.KEY: data.friend_uuid}}
            result = collection.update_one({"_id": ObjectId(data.user_uuid)}, add_friend_update)

            if result.matched_count == 0:
                raise NotFound("User")
            if result.matched_count == 1 and result.modified_count == 0:
                raise InternalError("Error in adding friend")

    async def remove_friend(self, data: RemoveFriendRepository.Input) -> None:
        friend_update = {"$pull": {self.KEY: data.friend_uuid}}

        with MongoConnection() as collection:
            result = collection.find_one({
                "_id": ObjectId(data.user_uuid),
                self.KEY: data.friend_uuid
            })

            if not result:
                raise NotFound("Friend")

            friend_uuid = result[self.KEY][0]
            result = collection.update_one({"_id": ObjectId(data.user_uuid)}, friend_update)

            if result.matched_count == 0:
                raise NotFound("User")

            if result.matched_count == 1 and result.modified_count == 0:
                raise InternalError("Error in removing friend")

            return friend_uuid
