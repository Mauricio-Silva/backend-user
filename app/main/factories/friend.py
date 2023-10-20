from app.data.usecases.friend import (
    DbListFriends,
    DbAddFriend,
    DbRemoveFriend,
)
from app.infra.mongo import FriendMongoRepository


def make_db_list_friends() -> DbListFriends:
    friend_mongo_repository = FriendMongoRepository()
    return DbListFriends(friend_mongo_repository)


def make_db_add_friend() -> DbAddFriend:
    friend_mongo_repository = FriendMongoRepository()
    return DbAddFriend(friend_mongo_repository)


def make_db_remove_friend() -> DbRemoveFriend:
    friend_mongo_repository = FriendMongoRepository()
    return DbRemoveFriend(friend_mongo_repository)
