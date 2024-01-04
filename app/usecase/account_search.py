from app.infra.mongo.projections import ADMIN_PROJECTION
from pymongo.collection import Collection
from app.domain.models import AccountOut
import re


class AccountSearch:
    KEY = "email"

    def __init__(self, collection: Collection, value: str, threshold: float) -> None:
        self.collection = collection
        self.value = value.lower().strip()
        self.threshold = threshold

    def compare(self, value: str) -> bool:
        if value is None or len(value) == 0:
            return False
        value = value.lower().strip()
        if self.value in value:
            return True
        if re.search(self.value, value):
            return True

    def filter(self, data: dict) -> bool:
        if self.compare(data[self.KEY]):
            return True
        else:
            return False

    def search(self) -> list[AccountOut]:
        result = self.collection.find_one({self.KEY: self.value}, ADMIN_PROJECTION)

        if result:
            return [AccountOut(**result)]

        results = self.collection.find({}, ADMIN_PROJECTION)

        return [AccountOut(**data) for data in results if self.filter(data)]
