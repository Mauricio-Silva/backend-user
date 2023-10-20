from app.domain.usecases import DeleteUser
from app.data.protocols import DeleteUserRepository


class DbDeleteUser(DeleteUser):
    def __init__(
        self,
        delete_user_repository: DeleteUserRepository
    ) -> None:
        self.__delete_user_repository = delete_user_repository

    async def delete(self, uuid: str) -> None:
        await self.__delete_user_repository.delete(uuid)
