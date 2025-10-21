# This is free and unencumbered software released into the public domain.

from base64 import b64encode, b64decode
from typing import override
from pydantic import Field, computed_field
from typing import ClassVar
from typing_extensions import Self
from .thing import Thing
import PIL.Image


class Image(Thing):
    model_label: ClassVar[str] = "Image"

    type: str = Field("Image", alias="@type")
    width: int | None = None
    height: int | None = None
    data_url: str | None = Field(default=None, alias="data")

    def __init__(self, id: str | None = None, **kwargs: object):
        super().__init__(id, **kwargs)

    @computed_field
    @property
    def data(self) -> bytes | None:
        if self.data_url:
            return b64decode(self.data_url.split(",")[1])
        return None

    @data.setter
    def data(self, new_data: bytes):
        self.data_url = f"data:image/rgb;base64,{b64encode(new_data).decode()}"

    def decode(self) -> PIL.Image.Image | None:
        if self.width and self.height and self.data:
            return PIL.Image.frombytes("RGB", (self.width, self.height), self.data)
        return None

    @override
    def metadata(self) -> Self:
        return self.without_data()

    def without_data(self) -> Self:
        return self.model_copy(update={"data": None, "data_url": None})
