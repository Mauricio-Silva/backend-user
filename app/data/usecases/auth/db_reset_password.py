from app.domain.usecases import ResetPassword
from app.data.protocols import (
    GetUserByUniqueRepository,
    EncodeTokenRepository,
    EncodeTokenInput,
    ResetPasswordRepository
)
from app.main.exceptions import NotFound
from app.main.config import CONTEXT_VAR


class DbResetPassword(ResetPassword):
    def __init__(
        self,
        get_user_by_unique_repository: GetUserByUniqueRepository,
        encode_token_repository: EncodeTokenRepository,
        reset_password_repository: ResetPasswordRepository
    ) -> None:
        self.__get_user_by_unique_repository = get_user_by_unique_repository
        self.__encode_token_repository = encode_token_repository
        self.__reset_password_repository = reset_password_repository

    async def reset_password(self, data: ResetPassword.Input) -> None:
        user = await self.__get_user_by_unique_repository.get_by_unique(data.email)

        if not user:
            raise NotFound("User")

        encode_token_input = EncodeTokenInput(url=CONTEXT_VAR.get(), uuid=str(user.uuid))
        access_token = self.__encode_token_repository.encode_token(encode_token_input)

        # TODO: set the frontend-url
        email = ResetPassword.Email(
            to=data.email,
            subject="Redefinição de Senha",
            username=user.username,
            link=f"frontend-url?token={access_token}"
        )

        await self.__reset_password_repository.reset_password(email)
