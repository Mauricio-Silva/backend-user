from pydantic import BaseModel, ConfigDict, Field, field_serializer
from app.schemas.common import OBJECT_UUID
from bson import ObjectId


class LoginModelOut(BaseModel):
    uuid: OBJECT_UUID
    username: str
    access_token: str

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @field_serializer('uuid')
    def serialize_uuid(self, uuid: ObjectId):
        return str(ObjectId(uuid))


class TokenModelOut(BaseModel):
    issuer: str = Field(validation_alias="iss")
    subject: str = Field(validation_alias="sub")
    expiration: int = Field(validation_alias="exp")
    service: str = Field(default="backend-user")


class AccountOut(BaseModel):
    uuid: OBJECT_UUID = Field(validation_alias="_id")
    name: str
    username: str
    email: str

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @field_serializer('uuid')
    def serialize_uuid(self, uuid: ObjectId):
        return str(ObjectId(uuid))
