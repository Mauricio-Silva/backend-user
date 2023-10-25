from typing import Any, cast
from pydantic import BaseModel

ha = cast(
    Any,
    {
        "authorizationUrl": "authorizationUrl",
        "tokenUrl": "tokenUrl",
        "refreshUrl": "refreshUrl",
        "scopes": {"scope1": "role1", "scope2": "role2"},
    },
)

# print(ha)


x = bool(None) or all([True, True])

# print(x)


class A1(BaseModel):
    a: int
    b: int
    c: int
    d: int
    e: int


class B1(BaseModel):
    a: int
    b: int


def t(data: B1):
    print(data.model_dump(exclude={"a"}))


x = A1(a=1, b=2, c=3, d=4, e=5)
t(x)

y = B1(**x.model_dump())
print(y)
