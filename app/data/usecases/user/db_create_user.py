from app.domain.usecases import CreateUser, GetUserInput
from app.data.protocols import (
    HashUserPasswordRepository,
    GetUserByUniqueRepository,
    CreateUserRepository
)
from app.main.exceptions import NotFound


class DbCreateUser(CreateUser):
    def __init__(
        self,
        hash_user_password_repository: HashUserPasswordRepository,
        check_user_by_unique_repository: GetUserByUniqueRepository,
        create_user_repository: CreateUserRepository
    ) -> None:
        self.__hash_user_password_repository = hash_user_password_repository
        self.__check_user_by_unique_repository = check_user_by_unique_repository
        self.__create_user_repository = create_user_repository

    async def create(self, data: CreateUser.Input) -> CreateUser.Output:
        data.password = self.__hash_user_password_repository.hash_password(data.password)

        get_user_input = GetUserInput(username=data.username, email=data.email)
        await self.__check_user_by_unique_repository.check_unique(get_user_input)

        user = await self.__create_user_repository.create(data)

        if user is None:
            raise NotFound("User")

        return user
