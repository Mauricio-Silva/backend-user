from app.schemas.common import DATETIME
from pydantic import BaseModel


class VideoModelOut(BaseModel):
    uuid: str
    url: str
    blob: str
    upload_at: DATETIME


class PhotoModelOut(BaseModel):
    url: str
    blob: str
    upload_at: DATETIME
