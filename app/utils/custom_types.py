from typing import Annotated
from pydantic import constr
from .patterns import (
    UUID_REGEX,
    QUERY_SEARCH_REGEX,
    NAME_REGEX,
    USERNAME_REGEX,
    EMAIL_REGEX,
    PASSWORD_REGEX,
    BIO_REGEX,
    URL_REGEX,
    PHONE_REGEX
)


UUID_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    strict=True,
    min_length=24,
    max_length=24,
    pattern=UUID_REGEX
)]

SEARCH_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    min_length=1,
    pattern=QUERY_SEARCH_REGEX
)]

NAME_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    min_length=3,
    max_length=70,
    pattern=NAME_REGEX
)]

USERNAME_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    min_length=6,
    max_length=12,
    pattern=USERNAME_REGEX
)]

EMAIL_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    min_length=7,
    max_length=70,
    pattern=EMAIL_REGEX
)]

PASSWORD_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    min_length=6,
    max_length=20,
    pattern=PASSWORD_REGEX
)]

BIO_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    max_length=255,
    pattern=BIO_REGEX
)]

URL_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    pattern=URL_REGEX
)]

PHONE_VALIDATOR = Annotated[str, constr(
    strip_whitespace=True,
    min_length=11,
    max_length=11,
    pattern=PHONE_REGEX
)]
