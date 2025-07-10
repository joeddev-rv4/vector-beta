from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    model: str
    description: str

class OuterArrayData(BaseModel):
    data: List[Item]

