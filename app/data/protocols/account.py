from abc import ABCMeta, abstractmethod
from app.domain.usecases import (
    UpdatePassword,
    ResetPassword,
    SetNewPassword,
    CheckUserEmail,
    ValidateUserEmail
)


class GetPasswordByUuidRepository(metaclass=ABCMeta):
    @abstractmethod
    async def get_by_id(self, uuid: str) -> str:
        pass


class UpdatePasswordRepository(metaclass=ABCMeta):
    Input = UpdatePassword.Input

    @abstractmethod
    async def update_password(self, data: Input) -> None:
        pass


class ResetPasswordRepository(metaclass=ABCMeta):
    Input = ResetPassword.Input

    @abstractmethod
    async def reset_password(self, data: Input) -> None:
        pass


class SetNewPasswordRepository(metaclass=ABCMeta):
    Input = SetNewPassword.Input

    @abstractmethod
    async def set_new_password(self, data: Input) -> None:
        pass


class CheckUserEmailRepository(metaclass=ABCMeta):
    Input = CheckUserEmail.Email

    @abstractmethod
    async def verify_email(self, data: Input) -> None:
        pass


class ValidateAccountRepository(metaclass=ABCMeta):
    Output = ValidateUserEmail.Output

    @abstractmethod
    async def validate(self, uuid: str) -> Output:
        pass
