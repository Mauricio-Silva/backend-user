from app.main.exceptions import FailedDependency
from app.main.config import EMAIL_SERVICE_BASE_URL
from ping3.errors import PingError
from fastapi import Request
from ping3 import ping


class EmailApi:
    MESSAGE = "Email service unavailable"

    async def __call__(self, _: Request):
        prefix = EMAIL_SERVICE_BASE_URL.removeprefix("http://")
        suffix = prefix.find(":")
        host = prefix[:suffix]

        try:
            if not ping(host):
                raise FailedDependency(self.MESSAGE)
        except PingError:
            raise FailedDependency(self.MESSAGE)
        except PermissionError:
            raise FailedDependency(self.MESSAGE)
