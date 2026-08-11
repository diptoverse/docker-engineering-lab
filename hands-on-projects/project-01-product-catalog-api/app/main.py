from fastapi import FastAPI

from app.database import engine
from app.models.base import Base
from app.models.product import Product 
from app.routers import products

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(products.router)

@app.get("/")
def root():
    return {"message": "Product Catalog API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}