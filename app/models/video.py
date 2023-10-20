from pydantic import BaseModel, Field
from datetime import datetime


class AddVideoDocument(BaseModel):
    url: str = Field()
    uuid: str | None = Field(default=None)
    create_at: datetime = Field(default=datetime.now())
