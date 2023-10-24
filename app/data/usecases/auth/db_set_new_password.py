from app.domain.usecases import SetNewPassword
from app.data.protocols import (
    HashUserPasswordRepository,
    SetNewPasswordRepository
)


class DbSetNewPassword(SetNewPassword):
    def __init__(
        self,
        hash_user_password_repository: HashUserPasswordRepository,
        set_new_password_repository: SetNewPasswordRepository
    ) -> None:
        self.__hash_user_password_repository = hash_user_password_repository
        self.__set_new_password_repository = set_new_password_repository

    async def reset_password(self, data: SetNewPassword.Input) -> None:
        data.password = self.__hash_user_password_repository.hash_password(data.password)
        await self.__set_new_password_repository.set_new_password(data)
