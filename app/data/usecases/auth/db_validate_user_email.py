from app.domain.usecases import ValidateUserEmail
from app.data.protocols import EnableUserRepository
from app.main.exceptions import NotFound


class DbValidateUserEmail(ValidateUserEmail):
    def __init__(
        self,
        enable_user_email_repository: EnableUserRepository
    ) -> None:
        self.__enable_user_email_repository = enable_user_email_repository

    async def validate_email(self, uuid: str) -> None:
        user = await self.__enable_user_email_repository.enable(uuid)

        if user is None:
            raise NotFound("User")
