import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.product import Product
from app.schemas.product import ProductResponse, ProductCreate
from app.redis_client import redis_client

router = APIRouter()


@router.get("/products", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.get("/products/{id}", response_model=ProductResponse)
def get_product(id: int, db: Session = Depends(get_db)):
    cache_key = f"product:{id}"

    cached_product = redis_client.get(cache_key)

    if cached_product:
        print("Cache Hit")
        return json.loads(str(cached_product))

    print("Cache Miss")

    product = db.query(Product).filter(Product.id == id).first()

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product_data = {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "stock": product.stock,
    }

    redis_client.set(
        cache_key,
        json.dumps(product_data)
    )
    
    return product

@router.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(
        name=product.name,
        price=product.price,
        stock=product.stock,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@router.put("/products/{id}", response_model=ProductResponse)
def update_product(
    id: int,
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    existing_product = db.query(Product).filter(Product.id == id).first()

    if existing_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    existing_product.name = product.name
    existing_product.price = product.price
    existing_product.stock = product.stock

    db.commit()
    db.refresh(existing_product)

    redis_client.delete(f"product:{id}")

    return existing_product

@router.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product)
    db.commit()

    redis_client.delete(f"product:{id}")
    print("Cache Invalidated", id)

    return {
        "message": "Product deleted successfully"
    }