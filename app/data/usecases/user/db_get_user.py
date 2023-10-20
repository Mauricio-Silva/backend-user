from app.domain.usecases import GetUserByUuid
from app.data.protocols import GetUserByUuidRepository


class DbGetUser(GetUserByUuid):
    def __init__(
        self,
        get_user_by_id_repository: GetUserByUuidRepository
    ) -> None:
        self.__get_user_by_id_repository = get_user_by_id_repository

    async def get_by_id(self, user_id: str) -> GetUserByUuid.Output:
        return await self.__get_user_by_id_repository.get_by_id(user_id)
