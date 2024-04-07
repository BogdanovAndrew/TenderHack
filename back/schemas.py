from pydantic import BaseModel

class STE(BaseModel):
    chars: list[str]
    fullname: str