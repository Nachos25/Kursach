from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_

from ..database import get_db
from ..models import Product, Category, Brand
from ..schemas import ProductPublic, CategoryPublic, BrandPublic

router = APIRouter(prefix="/api", tags=["catalog"])


@router.get("/brands", response_model=List[BrandPublic])
def list_brands(db: Session = Depends(get_db)):
    return db.query(Brand).order_by(Brand.name).all()


@router.get("/categories", response_model=List[CategoryPublic])
def list_categories(db: Session = Depends(get_db)):
    return db.query(Category).order_by(Category.name).all()


@router.get("/products", response_model=List[ProductPublic])
def list_products(
    db: Session = Depends(get_db),
    q: Optional[str] = Query(default=None, description="Пошук за назвою"),
    category: Optional[str] = None,
    brand: Optional[str] = None,
    limit: int = 30,
    offset: int = 0,
):
    query = db.query(Product)
    if q:
        like = f"%{q}%"
        query = query.filter(or_(Product.name.ilike(like), Product.short_desc.ilike(like)))
    if category:
        query = query.join(Product.category).filter(Category.slug == category)
    if brand:
        query = query.join(Product.brand).filter(Brand.slug == brand)

    products = query.offset(offset).limit(limit).all()
    return products


@router.get("/products/{slug}", response_model=ProductPublic)
def get_product(slug: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.slug == slug).first()
    return product




