# This is free and unencumbered software released into the public domain.

from pydantic import BaseModel, Field
from .percept import VisualPercept


class Observation(BaseModel):
    type: str = Field("Observation", alias="@type")
    id: str = Field(..., alias="@id")
    source: str | None = None
    percepts: list[VisualPercept] | None = None

    def to_json(self) -> str:
        import json

        return json.dumps(self.to_dict(), separators=(",", ":"))

    def to_dict(self) -> dict[str, object]:
        return self.model_dump(by_alias=True, exclude_computed_fields=True)
