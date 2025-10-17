# This is free and unencumbered software released into the public domain.

from pydantic import BaseModel, Field
from typing import Any, Optional
from . import VisualPercept


class Observation(BaseModel):
    type: str = Field("Observation", alias="@type")
    id: str = Field(..., alias="@id")
    source: Optional[str] = None
    percepts: Optional[list[VisualPercept]] = None

    def to_json(self) -> str:
        import json

        return json.dumps(self.to_dict(), separators=(",", ":"))

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump(by_alias=True, exclude_computed_fields=True)
