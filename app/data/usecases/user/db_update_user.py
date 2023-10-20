from app.domain.usecases import UpdateUser
from app.data.protocols import UpdateUserRepository


class DbUpdateUser(UpdateUser):
    def __init__(
        self,
        update_user_repository: UpdateUserRepository
    ) -> None:
        self.__update_user_repository = update_user_repository

    async def update(self, data: UpdateUser.Input) -> UpdateUser.Output:
        return await self.__update_user_repository.update(data)
