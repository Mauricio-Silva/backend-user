from app.domain.usecases import SearchAccounts
from app.data.protocols import SearchAccountsRepository
from app.main.exceptions import NotFound


class DbSearchAccounts(SearchAccounts):
    def __init__(
        self,
        search_accounts_repository: SearchAccountsRepository
    ) -> None:
        self.__search_accounts_repository = search_accounts_repository

    async def search(self, data: str) -> SearchAccounts.Output:
        accounts = await self.__search_accounts_repository.search(data)

        if accounts is None:
            raise NotFound("Account(s)")

        return accounts
