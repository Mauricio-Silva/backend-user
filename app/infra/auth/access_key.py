from app.main.exceptions import Unauthorized
from app.main.config import ACCESS_KEY
from fastapi import Header, Request


class AccessKey:
    KEY = Header(
        default=None,
        alias="access-key-bearer",
        description="The Admin Access Key Bearer"
    )

    async def __call__(self, request: Request, access_key: str = KEY):
        if access_key:
            if access_key != ACCESS_KEY:
                raise Unauthorized("Invalid access key")
            else:
                return None

        authorization = request.headers.get("Authorization")

        if not authorization:
            raise Unauthorized("No access key provided")

        scheme, _, credentials = authorization.partition(" ")

        if not (scheme and credentials):
            raise Unauthorized("No access key provided")

        if scheme.lower() != "bearer":
            raise Unauthorized("Invalid authentication scheme")

        if access_key != ACCESS_KEY:
            raise Unauthorized("Invalid access key")
