from pydantic import BaseModel

class Product(BaseModel):
    sku: str
    name: str
    description: str
    available_units: int
    unit_price: float

