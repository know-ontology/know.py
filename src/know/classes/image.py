# This is free and unencumbered software released into the public domain.

from base64 import b64encode, b64decode
from pydantic import BaseModel, Field, computed_field
import PIL.Image


class Image(BaseModel):
    type: str = Field("Image", alias="@type")
    id: str = Field(..., alias="@id")
    width: int
    height: int
    data_url: str = Field(..., alias="data")

    @computed_field
    @property
    def data(self) -> bytes:
        return b64decode(self.data_url.split(",")[1])

    @data.setter
    def data(self, new_data: bytes):
        self.data_url = f"data:image/rgb;base64,{b64encode(new_data).decode()}"

    def decode(self) -> PIL.Image:
        return PIL.Image.frombytes("RGB", (self.width, self.height), self.data)
