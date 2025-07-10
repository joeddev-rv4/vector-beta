from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    origin: str
    message: str

class FAQResponse(BaseModel):
    category: str
    chunk: str

