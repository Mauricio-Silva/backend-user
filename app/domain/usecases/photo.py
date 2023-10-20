from pydantic import BaseModel
from abc import ABCMeta, abstractmethod
from app.schemas.photo import OperationType


class ManagePhotoInput(BaseModel):
    user_uuid: str
    photo_url: str


class ManagePhoto(metaclass=ABCMeta):
    Input = ManagePhotoInput
    Output = OperationType

    @abstractmethod
    async def manage_photo(self, data: Input) -> Output:
        pass
