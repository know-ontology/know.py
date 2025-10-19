# This is free and unencumbered software released into the public domain.

from base64 import b64encode, b64decode
from pydantic import BaseModel, Field, computed_field
from typing_extensions import Self
import PIL.Image


class Image(BaseModel):
    type: str = Field("Image", alias="@type")
    id: str = Field(..., serialization_alias="@id")
    width: int | None = None
    height: int | None = None
    data_url: str | None = Field(default=None, alias="data")

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

    def metadata(self) -> Self:
        return self.without_data()

    def without_data(self) -> Self:
        return self.model_copy(update={"data": None, "data_url": None})

    def to_json(self) -> str:
        import json

        return json.dumps(self.to_dict(), separators=(",", ":"))

    def to_dict(self) -> dict[str, object]:
        return self.model_dump(
            by_alias=True,
            exclude_unset=True,
            exclude_none=True,
            exclude_computed_fields=True,
        )
