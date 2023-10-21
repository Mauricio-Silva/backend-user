from app.domain.usecases import PersonalProfile
from app.data.protocols import PersonalProfileRepository
from app.main.exceptions import NotFound


class DbPersonalProfile(PersonalProfile):
    def __init__(
        self,
        personal_profile_repository: PersonalProfileRepository
    ) -> None:
        self.__personal_profile_repository = personal_profile_repository

    async def get_personal_profile(self, uuid: str) -> PersonalProfile.Output:
        profile = await self.__personal_profile_repository.get_personal_profile(uuid)

        if not profile:
            raise NotFound("Profile")

        return profile
