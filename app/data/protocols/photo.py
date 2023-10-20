from abc import ABCMeta, abstractmethod
from app.domain.usecases import ManagePhoto


class ManagePhotoRepository(metaclass=ABCMeta):
    Input = ManagePhoto.Input
    Output = ManagePhoto.Output

    @abstractmethod
    async def manage_photo(self, data: Input) -> Output:
        pass
