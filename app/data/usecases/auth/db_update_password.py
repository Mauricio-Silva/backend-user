from app.domain.usecases import UpdatePassword
from app.data.protocols import (
    GetPasswordByUuidRepository,
    CheckUserPasswordRepository,
    HashUserPasswordRepository,
    UpdatePasswordRepository
)
from app.main.exceptions import NotFound, Forbidden


class DbUpdatePassword(UpdatePassword):
    def __init__(
        self,
        get_password_by_uuid_repository: GetPasswordByUuidRepository,
        check_user_password_repository: CheckUserPasswordRepository,
        hash_user_password_repository: HashUserPasswordRepository,
        update_password_repository: UpdatePasswordRepository
    ) -> None:
        self.__get_password_by_uuid_repository = get_password_by_uuid_repository
        self.__check_user_password_repository = check_user_password_repository
        self.__hash_user_password_repository = hash_user_password_repository
        self.__update_password_repository = update_password_repository

    async def update_password(self, data: UpdatePassword.Input) -> None:
        password = await self.__get_password_by_uuid_repository.get_by_id(data.uuid)

        if not password:
            raise NotFound("User")

        valid_password = self.__check_user_password_repository.verify_password(data.old_password, password)

        if not valid_password:
            raise Forbidden("Invalid password")

        data.new_password = self.__hash_user_password_repository.hash_password(data.new_password)

        await self.__update_password_repository.update_password(data)
