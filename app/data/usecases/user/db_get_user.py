from app.domain.usecases import GetUserByUuid
from app.data.protocols import GetUserByUuidRepository
from app.main.exceptions import NotFound


class DbGetUser(GetUserByUuid):
    def __init__(
        self,
        get_user_by_id_repository: GetUserByUuidRepository
    ) -> None:
        self.__get_user_by_id_repository = get_user_by_id_repository

    async def get_by_id(self, user_id: str) -> GetUserByUuid.Output:
        user = await self.__get_user_by_id_repository.get_by_id(user_id)

        if user is None:
            raise NotFound("User")

        return user
