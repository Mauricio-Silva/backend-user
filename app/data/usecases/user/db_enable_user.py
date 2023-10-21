from app.domain.usecases import EnableUser
from app.data.protocols import EnableUserRepository
from app.main.exceptions import NotFound


class DbEnableUser(EnableUser):
    def __init__(
        self,
        enable_user_repository: EnableUserRepository
    ) -> None:
        self.__enable_user_repository = enable_user_repository

    async def enable(self, uuid: str) -> EnableUser.Output:
        user = await self.__enable_user_repository.enable(uuid)

        if user is None:
            raise NotFound("User")

        return user
