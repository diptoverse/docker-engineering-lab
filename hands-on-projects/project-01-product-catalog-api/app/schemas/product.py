from pydantic import BaseModel, ConfigDict

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int

class ProductResponse(ProductCreate):
    id: int 

    model_config = ConfigDict(from_attributes=True)
