from pydantic import BaseModel
from app.domain.models import TokenModelOut
from abc import ABCMeta, abstractmethod


class HashUserPasswordRepository(metaclass=ABCMeta):
    @abstractmethod
    def hash_password(self, plain_password: str) -> str:
        pass


class CheckUserPasswordRepository(metaclass=ABCMeta):
    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        pass


class EncodeTokenInput(BaseModel):
    url: str
    uuid: str


class EncodeTokenRepository(metaclass=ABCMeta):
    Input = EncodeTokenInput

    @abstractmethod
    def encode_token(self, data: Input) -> str:
        pass


class DecodeTokenRepository(metaclass=ABCMeta):
    Output = TokenModelOut

    @abstractmethod
    def decode_token(self, token: str) -> Output:
        pass
