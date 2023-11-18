from app.domain.usecases import GetToken
from app.data.protocols import (
    GetUserByUniqueRepository,
    EncodeTokenRepository,
    EncodeTokenInput
)
from app.domain.models import LoginModelOut
from app.main.exceptions import NotFound
from fastapi import Request


class DbGetToken(GetToken):
    def __init__(
        self,
        request: Request,
        get_user_by_unique_repository: GetUserByUniqueRepository,
        encode_token_repository: EncodeTokenRepository
    ) -> None:
        self.__request = request
        self.__get_user_by_unique_repository = get_user_by_unique_repository
        self.__encode_token_repository = encode_token_repository

    async def get_token(self, data: GetToken.Input) -> GetToken.Output:
        user = await self.__get_user_by_unique_repository.get_by_unique(data.username_or_email)

        if not user:
            raise NotFound("User")

        encode_token_input = EncodeTokenInput(url=f"{self.__request.base_url}snapcut/api", uuid=str(user.uuid))
        access_token = self.__encode_token_repository.encode_token(encode_token_input)

        return LoginModelOut(uuid=user.uuid, username=user.username, access_token=access_token)
