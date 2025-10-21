# This is free and unencumbered software released into the public domain.

from pydantic import Field
from typing import ClassVar
from .thing import Thing


class Percept(Thing):
    model_label: ClassVar[str] = "Percept"

    type: str = Field("Percept", alias="@type")

    def __init__(self, id: str | None = None, **kwargs: object):
        super().__init__(id, **kwargs)


class VisualPercept(Percept):
    model_label: ClassVar[str] = "Visual Percept"

    type: str = Field("VisualPercept", alias="@type")
    source: str | None = None
    subject: str
    confidence: float | None = None
    box: str | None = None

    def __init__(self, id: str | None = None, **kwargs: object):
        super().__init__(id, **kwargs)
