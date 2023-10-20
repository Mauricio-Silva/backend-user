from app.domain.usecases import EnableUser
from app.data.protocols import EnableUserRepository


class DbEnableUser(EnableUser):
    def __init__(
        self,
        enable_user_repository: EnableUserRepository
    ) -> None:
        self.__enable_user_repository = enable_user_repository

    async def enable(self, uuid: str) -> EnableUser.Output:
        return await self.__enable_user_repository.enable(uuid)
