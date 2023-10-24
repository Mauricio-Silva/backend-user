from typing import Any, cast


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

print(x)
