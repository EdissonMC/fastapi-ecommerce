from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True
