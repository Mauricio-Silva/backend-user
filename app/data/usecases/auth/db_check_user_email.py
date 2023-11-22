from app.domain.usecases import CheckUserEmail
from app.data.protocols import (
    EncodeTokenRepository,
    CheckUserEmailRepository,
    EncodeTokenInput
)
from app.main.config import CONTEXT_VAR


class DbCheckUserEmail(CheckUserEmail):
    def __init__(
        self,
        encode_token_repository: EncodeTokenRepository,
        check_user_email_repository: CheckUserEmailRepository
    ) -> None:
        self.__encode_token_repository = encode_token_repository
        self.__check_user_email_repository = check_user_email_repository

    async def verify_email(self, data: CheckUserEmail.Input) -> None:
        encode_token_input = EncodeTokenInput(url=CONTEXT_VAR.get(), uuid=str(data.uuid))

        access_token = self.__encode_token_repository.encode_token(encode_token_input)
        # TODO: create endpoint to receive this
        email = CheckUserEmail.Email(
            to=data.email,
            subject="Confirmação de conta",
            username=data.username,
            link=f"frontend-url?token={access_token}"
        )

        await self.__check_user_email_repository.verify_email(email)
