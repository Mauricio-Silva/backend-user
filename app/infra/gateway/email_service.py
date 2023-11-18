from app.data.protocols import (
    ResetPasswordRepository,
    CheckUserEmailRepository,
    ResendEmailRepository
)
from app.main.exceptions import FailedDependency
from .httpx_helper import HttpxHelper
from time import sleep


class EmailService(
    HttpxHelper,
    ResetPasswordRepository,
    CheckUserEmailRepository,
    ResendEmailRepository
):
    def __init__(self):
        super().__init__()

    async def reset_password(self, data: ResetPasswordRepository.Input) -> None:
        body = data.model_dump()
        await self.api_call("reset_password", body)

    async def verify_email(self, data: CheckUserEmailRepository.Input) -> None:
        body = data.model_dump()
        for count in range(4):
            try:
                await self.api_call("account_confirmation", body)
                break
            except FailedDependency as error:
                if count < 3:
                    sleep(5)
                else:
                    raise error

    async def resend_email(self, data: ResendEmailRepository.Input) -> None:
        body = data.model_dump()
        await self.api_call("account_confirmation", body)
