from app.domain.usecases import ResetPassword
from app.data.protocols import (
    GetUserByUniqueRepository,
    EncodeTokenRepository,
    EncodeTokenInput,
    ResetPasswordRepository
)
from app.main.exceptions import NotFound
from fastapi import Request


class DbResetPassword(ResetPassword):
    def __init__(
        self,
        request: Request,
        get_user_by_unique_repository: GetUserByUniqueRepository,
        encode_token_repository: EncodeTokenRepository,
        reset_password_repository: ResetPasswordRepository
    ) -> None:
        self.__request = request
        self.__get_user_by_unique_repository = get_user_by_unique_repository
        self.__encode_token_repository = encode_token_repository
        self.__reset_password_repository = reset_password_repository

    async def reset_password(self, data: ResetPassword.Input) -> None:
        user = await self.__get_user_by_unique_repository.get_by_unique(data.email)

        if not user:
            raise NotFound("User")

        url = f"{self.__request.base_url}/snapcut/api"
        encode_token_input = EncodeTokenInput(url=url, uuid=str(user.uuid))
        access_token = self.__encode_token_repository.encode_token(encode_token_input)

        # TODO: set the frontend-url
        email = ResetPassword.Email(
            to=data.email,
            subject="Redefinição de Senha",
            username=data.username,
            link=f"frontend-url?token={access_token}"
        )

        await self.__reset_password_repository.reset_password(email)
