from app.domain.usecases import UserLogin
from app.data.protocols import (
    GetUserByUniqueRepository,
    CheckUserPasswordRepository,
    EncodeTokenRepository,
    EncodeTokenInput
)
from app.domain.models import LoginModelOut
from app.main.exceptions import NotFound, Forbidden
from fastapi import Request


class AuthLogin(UserLogin):
    def __init__(
        self,
        request: Request,
        get_user_by_unique_repository: GetUserByUniqueRepository,
        check_user_password_repository: CheckUserPasswordRepository,
        encode_token_repository: EncodeTokenRepository
    ) -> None:
        self.__request = request
        self.__get_user_by_unique_repository = get_user_by_unique_repository
        self.__check_user_password_repository = check_user_password_repository
        self.__encode_token_repository = encode_token_repository

    async def login(self, data: UserLogin.Input) -> UserLogin.Output:
        user = await self.__get_user_by_unique_repository.get_by_unique(data.username_or_email)

        if not user:
            raise NotFound("User")

        if not user.is_enabled:
            raise Forbidden("User account must be enabled")

        valid_password = self.__check_user_password_repository.verify_password(data.password, user.password)

        if not valid_password:
            raise Forbidden("Invalid password")

        encode_token_input = EncodeTokenInput(url=f"{self.__request.base_url}snapcut/api", uuid=str(user.uuid))
        access_token = self.__encode_token_repository.encode_token(encode_token_input)

        return LoginModelOut(uuid=user.uuid, username=user.username, access_token=access_token)
