from app.data.protocols import ResetPasswordRepository
from .httpx_helper import HttpxHelper


class EmailService(HttpxHelper, ResetPasswordRepository):
    RESET_PATH = "reset-password"

    def __init__(self):
        super().__init__()

    async def reset_password(self, data: ResetPasswordRepository.Input) -> None:
        body = data.model_dump()
        await self.api_call(self.RESET_PATH, body)
