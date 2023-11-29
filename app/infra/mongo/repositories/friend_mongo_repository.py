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

            friends = [] if user[self.KEY] is None else list(user[self.KEY])
            if data.friend_uuid in friends:
                raise Conflict("Friend already exists")

            friends.append(data.friend_uuid)
            add_friend_update = {"$set": {self.KEY: friends}}

            result = collection.update_one({"_id": ObjectId(data.user_uuid)}, add_friend_update)
            if result.matched_count == 0:
                raise NotFound("User")
            if result.matched_count == 1 and result.modified_count == 0:
                raise InternalError("Error in adding friend")

    async def remove_friend(self, data: RemoveFriendRepository.Input) -> None:
        with MongoConnection() as collection:
            user = collection.find_one({"_id": ObjectId(data.user_uuid)}, FRIENDS_PROJECTION)
            if user is None or not user[self.KEY]:
                return None

            friends = list(user[self.KEY])
            if data.friend_uuid not in friends:
                raise NotFound("Friend")

            friends.remove(data.friend_uuid)
            remove_friend_update = {"$set": {self.KEY: friends}}

            result = collection.update_one({"_id": ObjectId(data.user_uuid)}, remove_friend_update)
            if result.matched_count == 0:
                raise NotFound("User")
            if result.matched_count == 1 and result.modified_count == 0:
                raise InternalError("Error in removing friend")
