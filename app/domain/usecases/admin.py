from pydantic import BaseModel
from abc import ABCMeta, abstractmethod
from app.domain.models import AccountOut, LoginModelOut


class ResendEmailInput(BaseModel):
    email: str


class UserEmailInput(BaseModel):
    to: str
    subject: str
    username: str
    link: str


class ResendEmail(metaclass=ABCMeta):
    Input = ResendEmailInput
    Email = UserEmailInput

    @abstractmethod
    async def resend_email(self, data: Input) -> None:
        pass


class GetTokenInput(BaseModel):
    username_or_email: str


class GetToken(metaclass=ABCMeta):
    Input = GetTokenInput
    Output = LoginModelOut

    @abstractmethod
    async def get_token(self, data: Input) -> Output:
        pass


class SearchAccounts(metaclass=ABCMeta):
    Output = list[AccountOut] | None

    @abstractmethod
    async def search(self, data: str) -> Output:
        pass
