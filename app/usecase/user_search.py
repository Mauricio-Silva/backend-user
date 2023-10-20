from app.domain.models import UserModelOut
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz


class UserSearch:
    def __init__(self, value: str, threshold: float) -> None:
        self.value = value.lower().strip()
        self.threshold = threshold

    def compare(self, value: str) -> bool:
        if value is None or len(value) == 0:
            return False
        value = value.lower().strip()
        ratio1 = fuzz.ratio(self.value, value)
        ratio2 = SequenceMatcher(a=self.value, b=value).ratio()
        average = (((ratio1 / 100) * 6) + (ratio2 * 4)) / 10
        return average >= self.threshold

    def filter(self, user: dict) -> bool:
        if self.compare(user["username"]):
            return True
        elif self.compare(user.get("name", None)):
            return True
        else:
            return False

    def search(self, results: list[dict]) -> list[UserModelOut]:
        return [UserModelOut(**user) for user in results if self.filter(user)]
