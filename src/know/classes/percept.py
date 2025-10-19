# This is free and unencumbered software released into the public domain.

from pydantic import Field
from .thing import Thing


class Percept(Thing):
    type: str = Field("Percept", alias="@type")

    def __init__(self, id: str | None = None, **kwargs: object):
        super().__init__(id, **kwargs)


class VisualPercept(Percept):
    type: str = Field("VisualPercept", alias="@type")
    source: str | None = None
    subject: str
    confidence: float | None = None

    def __init__(self, id: str | None = None, **kwargs: object):
        super().__init__(id, **kwargs)
