# This is free and unencumbered software released into the public domain.

from base64 import b64decode
from pydantic import Field
from .thing import Thing


class AudioFrame(Thing):
    type: str = Field("AudioFrame", alias="@type")
    rate: int
    channels: int
    samples: int
    data_url: str = Field(..., alias="data")

    def __init__(self, id: str | None = None, **kwargs: object):
        super().__init__(id, **kwargs)

    @property
    def data(self) -> bytes:
        return b64decode(self.data_url.split(",")[1])
