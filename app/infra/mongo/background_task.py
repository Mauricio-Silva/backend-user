from app.main.config import EXPIRE_CHECK_ACCOUNT_TIME, MongoConnection
from .projections import DISABLE_ACCOUNTS
from datetime import datetime, timedelta
from app.utils.logger import Logger
from threading import Thread
from time import sleep


class BackgroundTask:
    def __init__(self) -> None:
        self.__shutdown = False
        self.__expire_time = timedelta(minutes=EXPIRE_CHECK_ACCOUNT_TIME)
        self.__thread = Thread(target=self.remove_disable_accounts)
        self.__thread.start()

    def thread_shutdown(self):
        self.__shutdown = True
        self.__thread.join()

    def __filter(self, data: dict):
        is_enabled = data["is_enabled"]
        create_at = data["create_at"]
        time_difference = datetime.now() - create_at
        is_time_expired = time_difference >= self.__expire_time
        if not is_enabled and is_time_expired:
            return True
        return False

    def remove_disable_accounts(self):
        while not self.__shutdown:
            print("Here")
            sleep(EXPIRE_CHECK_ACCOUNT_TIME * 60)
            with MongoConnection() as collection:
                results = collection.find({}, DISABLE_ACCOUNTS)
                if not results:
                    continue
                else:
                    for data in filter(self.__filter, results):
                        result = collection.delete_one({"_id": data["_id"]})
                        if result.deleted_count != 1:
                            Logger.error("Error in deleting user")
                        else:
                            Logger.info(f"User {data['_id']} deleted successfully")
