from abc import ABCMeta, abstractmethod
from app.domain.usecases import (
    ResendEmail,
    SearchAccounts
)


class ResendEmailRepository(metaclass=ABCMeta):
    Input = ResendEmail.Email

    @abstractmethod
    async def resend_email(self, data: Input) -> None:
        pass


class SearchAccountsRepository(metaclass=ABCMeta):
    Output = SearchAccounts.Output

    @abstractmethod
    async def search(self, data: str) -> Output:
        pass
