# This is free and unencumbered software released into the public domain.

from pydantic import BaseModel, Field
from typing import Any


class Thing(BaseModel):
    type: str = Field("Thing", alias="@type")
    id: str = Field(..., alias="@id")

    def to_json(self) -> str:
        import json

        return json.dumps(self.to_dict())

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump(by_alias=True, exclude_computed_fields=True)
