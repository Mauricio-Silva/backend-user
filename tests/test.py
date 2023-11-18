from typing import Any, cast
from time import sleep
import schedule
import sched
import time
import threading
import asyncio
import contextvars
import _thread


ha = cast(
    Any,
    {
        "authorizationUrl": "authorizationUrl",
        "tokenUrl": "tokenUrl",
        "refreshUrl": "refreshUrl",
        "scopes": {"scope1": "role1", "scope2": "role2"},
    },
)
# print(ha)


class AA:
    def make_usecase(self, **kwargs):
        instance = self.__class__()
        for key, value in kwargs.items():
            setattr(instance, key, value)
        return instance


class DbListUsers:
    def __init__(self, number: int) -> None:
        self.numer = number


class MakeDbListUsersSut(AA):
    def __init__(self) -> None:
        self.list_users_repository_spy = 12

    def make_usecase(self):
        self.usecase = DbListUsers(self.list_users_repository_spy)


a = MakeDbListUsersSut()
a.make_usecase()
# print(a.usecase)


def task():
    print("Doing")


schedule.every(5).seconds.do(task)

# while True:
#     print("Here")
#     schedule.run_pending()
#     sleep(1)


# s = sched.scheduler(time.time, time.sleep)
# s.enter(1, 1, task)
# s.run()


task_thread = threading.Thread(target=task)
task_thread.start()


_thread.start_new_thread(task, ())
