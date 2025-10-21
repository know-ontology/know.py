# This is free and unencumbered software released into the public domain.

from pydantic import Field
from typing import ClassVar
from .percept import Percept
from .thing import Thing


class Observation(Thing):
    model_label: ClassVar[str] = "Observation"

    type: str = Field("Observation", alias="@type")
    source: str | None = None
    percepts: list[Percept] = []

    def __init__(self, id: str | None = None, **kwargs: object):
        super().__init__(id, **kwargs)
