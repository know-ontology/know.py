# This is free and unencumbered software released into the public domain.

from base64 import b64decode
from pydantic import BaseModel, Field


class AudioFrame(BaseModel):
    type: str = Field("AudioFrame", alias="@type")
    id: str = Field(..., alias="@id")
    rate: int
    channels: int
    samples: int
    data_url: str = Field(..., alias="data")

    @property
    def data(self) -> bytes:
        return b64decode(self.data_url.split(",")[1])
