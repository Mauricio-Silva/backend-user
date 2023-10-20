from datetime import datetime
from pydantic import BaseModel, Field, field_serializer
from bson import ObjectId


class User(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, validation_alias="_id")
    name: str | None = Field(default=None)
    username: str | None = Field(default=None)
    email: str | None = Field(default=None)
    password: str | None = Field(default=None)
    bio: str | None = Field(default=None)
    create_at: datetime = Field(default=datetime.now())
    update_at: datetime = Field(default=datetime.now())
    videos: list | None = Field(default=None)
    friends: list | None = Field(default=None)
    verified_at: datetime = Field(default=datetime.now())

    class Config:
        arbitrary_types_allowed = True

    @field_serializer('id')
    def serialize_id(self, id: ObjectId):
        return str(ObjectId(id))


class UserData(BaseModel):
    id: str = Field(validation_alias="_id")
    name: None | str
    username: None | str
    email: None | str
    bio: None | str
    create_at: None | datetime
    update_at: None | datetime
    verified_at: None | datetime


class UserMapper:
    @staticmethod
    def to_output(data: dict):
        data["_id"] = str(ObjectId(data["_id"]))
        return UserData.model_validate(data)


DATA = {
    '_id': ObjectId('64dd88af4f98f0953e87db58'),
    'username': 'root',
    'email': 'root@gmail.com',
    'password': 'admin',
    'bio': 'oi sou o root',
    'create_at': datetime(2023, 8, 16, 22, 40, 47, 640000),
    'update_at': datetime(2023, 8, 16, 22, 40, 47, 640000),
    'videos': [],
    'friends': []
}

print(User(**DATA))
