from pydantic import BaseModel
from app.domain.models import LoginModelOut
from abc import ABCMeta, abstractmethod


class UserLoginInput(BaseModel):
    username_or_email: str
    password: str


class UserLogin(metaclass=ABCMeta):
    Input = UserLoginInput
    Output = LoginModelOut

    @abstractmethod
    async def login(self, data: Input) -> Output:
        pass
