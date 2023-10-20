from app.domain.usecases import ManagePhoto
from app.data.protocols import ManagePhotoRepository


class DbManagePhoto(ManagePhoto):
    def __init__(
        self,
        manage_photo_repository: ManagePhotoRepository
    ) -> None:
        self.__manage_photo_repository = manage_photo_repository

    async def manage_photo(self, data: ManagePhoto.Input) -> ManagePhoto.Output:
        return await self.__manage_photo_repository.manage_photo(data)
