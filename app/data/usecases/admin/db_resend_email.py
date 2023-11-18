from app.domain.usecases import ResendEmail
from app.data.protocols import (
    GetUserByUniqueRepository,
    EncodeTokenRepository,
    EncodeTokenInput,
    ResendEmailRepository
)
from app.main.exceptions import NotFound
from fastapi import Request


class DbResendEmail(ResendEmail):
    def __init__(
        self,
        request: Request,
        get_user_by_unique_repository: GetUserByUniqueRepository,
        encode_token_repository: EncodeTokenRepository,
        resend_email_repository: ResendEmailRepository
    ) -> None:
        self.__request = request
        self.__get_user_by_unique_repository = get_user_by_unique_repository
        self.__encode_token_repository = encode_token_repository
        self.__resend_email_repository = resend_email_repository

    async def resend_email(self, data: ResendEmail.Input) -> None:
        user = await self.__get_user_by_unique_repository.get_by_unique(data.email)

        if not user:
            raise NotFound("User")

        url = f"{self.__request.base_url}/snapcut/api"
        encode_token_input = EncodeTokenInput(url=url, uuid=str(user.uuid))
        access_token = self.__encode_token_repository.encode_token(encode_token_input)

        email = ResendEmail.Email(
            to=data.email,
            subject="Confirmação de conta",
            username=user.username,
            link=f"frontend-url?token={access_token}"
        )

        await self.__resend_email_repository.resend_email(email)
