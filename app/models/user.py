from pydantic import BaseModel, Field
from datetime import datetime


class CreateUserDocument(BaseModel):
    name: str = Field()
    username: str = Field()
    email: str | None = Field(default=None)
    password: str = Field()
    photo: str | None = Field(default=None)
    bio: str | None = Field(default=None)
    create_at: datetime = Field(default=datetime.now())
    update_at: datetime = Field(default=datetime.now())
    videos: list | None = Field(default=None)
    friends: list | None = Field(default=None)
    verified_at: datetime = Field(default=datetime.now())
    is_enabled: bool = Field(default=True)


class UpdateUserDocument(BaseModel):
    name: str | None = Field(default=None)
    username: str | None = Field(default=None)
    email: str | None = Field(default=None)
    photo: str | None = Field(default=None)
    bio: str | None = Field(default=None)
    update_at: datetime = Field(default=datetime.now())
