# This is free and unencumbered software released into the public domain.

from base64 import b64decode
from pydantic import BaseModel, Field
import PIL.Image


class Image(BaseModel):
    type: str = Field("Image", alias="@type")
    id: str = Field(..., alias="@id")
    width: int
    height: int
    data_url: str = Field(..., alias="data")

    @property
    def data(self) -> bytes:
        return b64decode(self.data_url.split(",")[1])

    def decode(self) -> PIL.Image:
        return PIL.Image.frombytes("RGB", (self.width, self.height), self.data)
