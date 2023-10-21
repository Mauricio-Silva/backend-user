from app.domain.usecases import DisableUser
from app.data.protocols import DisableUserRepository
from app.main.exceptions import NotFound


class DbDisableUser(DisableUser):
    def __init__(
        self,
        disable_user_repository: DisableUserRepository
    ) -> None:
        self.__disable_user_repository = disable_user_repository

    async def disable(self, uuid: str) -> DisableUser.Output:
        user = await self.__disable_user_repository.disable(uuid)

        if user is None:
            raise NotFound("User")

        return user
