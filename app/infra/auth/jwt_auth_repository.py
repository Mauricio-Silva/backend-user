from app.data.protocols import (
    HashUserPasswordRepository,
    CheckUserPasswordRepository,
    EncodeTokenRepository,
    DecodeTokenRepository
)
from app.main.config import JWT
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError, ExpiredSignatureError
from app.models import JwtEncoder
from app.main.exceptions import InternalError, Unauthorized
from app.domain.models import TokenModelOut


class JwtRepository(
    HashUserPasswordRepository,
    CheckUserPasswordRepository,
    EncodeTokenRepository,
    DecodeTokenRepository
):
    def __init__(self, reset_expire: int = None) -> None:
        self.__expire = JWT.expire if not reset_expire else reset_expire
        self.__crypt_context = CryptContext(schemes=[JWT.scheme], deprecated="auto")

    def hash_password(self, plain_password: str) -> str:
        return self.__crypt_context.hash(plain_password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.__crypt_context.verify(plain_password, hashed_password)

    def encode_token(self, data: EncodeTokenRepository.Input) -> str:
        expiration = datetime.utcnow() + timedelta(minutes=self.__expire)
        encoder = JwtEncoder(
            issuer=data.url,
            subject=f"uuid:{data.uuid.encode('utf-8').hex()}",
            expiration=expiration
        ).model_dump(by_alias=True)
        try:
            return jwt.encode(encoder, JWT.secret, algorithm=JWT.algorithm)
        except JWTError:
            raise InternalError("Error in encoding jwt token")

    def decode_token(self, token: str) -> DecodeTokenRepository.Output:
        try:
            decoder = jwt.decode(token, JWT.secret, algorithms=JWT.algorithm)
            model_out = TokenModelOut(**decoder)
            hex_subject = model_out.subject.removeprefix("uuid:")
            model_out.subject = bytes.fromhex(hex_subject).decode("utf-8")
            return model_out
        except ExpiredSignatureError:
            raise Unauthorized("Expired JWT token")
        except JWTError:
            raise Unauthorized("Invalid JWT token")
