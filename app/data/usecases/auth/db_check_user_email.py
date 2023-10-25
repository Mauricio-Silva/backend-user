from app.domain.usecases import CheckUserEmail
from app.data.protocols import (
    EncodeTokenRepository,
    CheckUserEmailRepository,
    EncodeTokenInput
)
from fastapi import Request


class DbCheckUserEmail(CheckUserEmail):
    def __init__(
        self,
        request: Request,
        encode_token_repository: EncodeTokenRepository,
        check_user_email_repository: CheckUserEmailRepository
    ) -> None:
        self.__request = request
        self.__encode_token_repository = encode_token_repository
        self.__check_user_email_repository = check_user_email_repository

    async def verify_email(self, data: CheckUserEmail.Input) -> None:
        url = f"{self.__request.base_url}/snapcut/api"
        encode_token_input = EncodeTokenInput(url=url, uuid=str(data.uuid))

        access_token = self.__encode_token_repository.encode_token(encode_token_input)
        # TODO: create endpoint to receive this
        data.url = f"<frontend-url>?token={access_token}"
        data = CheckUserEmail.Input(**data.model_dump())

        await self.__check_user_email_repository.verify_email(data)
