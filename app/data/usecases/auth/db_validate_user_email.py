from app.domain.usecases import ValidateUserEmail
from app.data.protocols import ValidateAccountRepository
from app.main.exceptions import NotFound


class DbValidateUserEmail(ValidateUserEmail):
    def __init__(
        self,
        validate_account_repository: ValidateAccountRepository
    ) -> None:
        self.__validate_account_repository = validate_account_repository

    async def validate_email(self, uuid: str) -> ValidateUserEmail.Output:
        user = await self.__validate_account_repository.validate(uuid)

        if user is None:
            raise NotFound("User")
