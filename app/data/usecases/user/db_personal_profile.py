from app.domain.usecases import PersonalProfile
from app.data.protocols import PersonalProfileRepository


class DbPersonalProfile(PersonalProfile):
    def __init__(
        self,
        personal_profile_repository: PersonalProfileRepository
    ) -> None:
        self.__personal_profile_repository = personal_profile_repository

    async def get_personal_profile(self, uuid: str) -> PersonalProfile.Output:
        return await self.__personal_profile_repository.get_personal_profile(uuid)
