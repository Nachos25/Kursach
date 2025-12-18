from fastapi import APIRouter, HTTPException
from typing import List
from service.product_service import ProductService
from pydantic import BaseModel, Field
from datetime import datetime

router = APIRouter()
service = ProductService()

# DTOs
class ProductCreateRequest(BaseModel):
    name: str = Field(..., example="Laptop")
    description: str = Field("", example="Gaming laptop")
    price: float = Field(..., example=1000)
    discount: float = Field(0.0, example=0.1)

class ProductUpdateRequest(BaseModel):
    name: str = None
    description: str = None
    price: float = None
    discount: float = None

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    discount: float
    created_at: datetime
    updated_at: datetime

class ErrorResponse(BaseModel):
    error: str
    code: str
    details: list = []

# Endpoints
@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/products", response_model=List[ProductResponse])
def list_products():
    return service.list_products()

@router.post("/products", response_model=ProductResponse, status_code=201)
def create_product(request: ProductCreateRequest):
    try:
        product = service.create_product(**request.dict())
        return product
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    product = service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, request: ProductUpdateRequest):
    try:
        product = service.update_product(product_id, **request.dict())
        return product
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):
    success = service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return
