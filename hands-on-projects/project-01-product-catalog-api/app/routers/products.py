from fastapi import APIRouter, HTTPException

from app.models.product import Product
from app.schemas.product import ProductCreate

router = APIRouter()

products = [
    Product(
        id=1,
        name="Laptop",
        price=120000.0,
        stock=10,
    ),
    Product(
        id=2,
        name="Keyboard",
        price=50.0,
        stock=25,
    )
]

@router.get("/products", response_model=list[Product])
def get_products():
    return products

@router.get("/products/{id}", response_model=Product)
def get_product(id: int):
    for product in products:
        if product.id == id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found in the list"
    )

@router.post("/products", response_model=Product)
def create_product(product: ProductCreate):
    new_product = Product(
        id=len(products) + 1,
        name=product.name,
        price=product.price,
        stock=product.stock,
    )

    products.append(new_product)
    return new_product

@router.put("/products/{id}", response_model=Product)
def update_product(id: int, product: ProductCreate):
    for index, existing_product in enumerate(products):
        if existing_product.id == id:
            updated_product = Product(
                id=id,
                name=product.name,
                price=product.price,
                stock=product.stock,
            )

            products[index] = updated_product

            return updated_product

    raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

@router.delete("/products/{id}")
def delete_product(id: int):
    for index, product in enumerate(products):
        if product.id == id:
            products.pop(index)

            return{
                "message": "Product deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )