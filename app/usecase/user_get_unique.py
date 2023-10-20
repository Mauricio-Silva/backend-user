from app.domain.models import UserLoginModelOut
from app.domain.usecases import GetUserByUnique
from pymongo.collection import Collection
from app.main.exceptions import Conflict
from app.infra.mongo.projections import LOGIN_MODEL_OUT_PROJECTION


class UserGetUnique:
    def __init__(self, collection: Collection) -> None:
        self.collection = collection

    def check_unique(self, data: GetUserByUnique.Input) -> None:
        usernames = self.collection.distinct("username")
        if data.username in list(usernames):
            raise Conflict("Username already exists")
        elif data.email:
            emails = self.collection.distinct("email")
            if data.email in emails:
                raise Conflict("Email already exists")

    def get_by_unique(self, username_or_email: str):
        result = self.collection.find_one({"username": username_or_email}, LOGIN_MODEL_OUT_PROJECTION)
        if not result:
            result = self.collection.find_one({"email": username_or_email}, LOGIN_MODEL_OUT_PROJECTION)
        return None if result is None else UserLoginModelOut(**result)
