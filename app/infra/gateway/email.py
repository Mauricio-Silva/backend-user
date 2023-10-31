from app.data.protocols import ResetPasswordRepository, CheckUserEmailRepository
from .httpx_helper import HttpxHelper


class EmailService(HttpxHelper, ResetPasswordRepository, CheckUserEmailRepository):
    def __init__(self):
        super().__init__()

    async def reset_password(self, data: ResetPasswordRepository.Input) -> None:
        body = data.model_dump()
        await self.api_call("reset_password", body)

    async def verify_email(self, data: CheckUserEmailRepository.Input) -> None:
        body = data.model_dump()
        await self.api_call("account_confirmation", body)
