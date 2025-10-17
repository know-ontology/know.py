# This is free and unencumbered software released into the public domain.

from base64 import b64decode
from pydantic import BaseModel, Field
from typing import Any


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

    def to_json(self) -> str:
        import json

        return json.dumps(self.to_dict(), separators=(",", ":"))

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump(by_alias=True, exclude_computed_fields=True)
