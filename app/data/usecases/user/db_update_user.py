from app.domain.usecases import UpdateUser
from app.data.protocols import UpdateUserRepository
from app.main.exceptions import NotFound


class DbUpdateUser(UpdateUser):
    def __init__(
        self,
        update_user_repository: UpdateUserRepository
    ) -> None:
        self.__update_user_repository = update_user_repository

    async def update(self, data: UpdateUser.Input) -> UpdateUser.Output:
        user = await self.__update_user_repository.update(data)

        if user is None:
            raise NotFound("User")

        return user
