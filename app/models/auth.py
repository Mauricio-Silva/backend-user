from pydantic import BaseModel, Field
from datetime import datetime


class JwtEncoder(BaseModel):
    issuer: str = Field(serialization_alias="iss", description="Service URL who issued JWT")
    subject: str = Field(serialization_alias="sub", description="User uuid Hash")
    expiration: datetime = Field(serialization_alias="exp", description="Expiration time")
    service: str = Field(default="backend-user", description="Service name")
