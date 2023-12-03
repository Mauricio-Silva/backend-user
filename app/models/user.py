from pydantic import BaseModel, Field
from datetime import datetime


class CreateUserDocument(BaseModel):
    name: str = Field()
    username: str = Field()
    email: str | None = Field(default=None)
    password: str = Field()
    phone: str | None = Field(default=None)
    photo: None = Field(default=None)
    bio: str | None = Field(default=None)
    create_at: datetime = Field(default=datetime.now())
    update_at: datetime = Field(default=datetime.now())
    videos: list | None = Field(default=None)
    friends: list | None = Field(default=None)
    verified_at: datetime | None = Field(default=None)
    is_enabled: bool = Field(default=False)


class UpdateUserDocument(BaseModel):
    name: str | None = Field(default=None)
    username: str | None = Field(default=None)
    email: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    bio: str | None = Field(default=None)
    update_at: datetime = Field(default=datetime.now())
