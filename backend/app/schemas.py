from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserBase(BaseModel):
    username: str
    email: EmailStr | None = None
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str = Field(min_length=6)


class UserPublic(UserBase):
    id: int
    is_admin: bool = False
    created_at: datetime

    class Config:
        from_attributes = True


class BrandPublic(BaseModel):
    id: int
    name: str
    slug: str
    logo_url: Optional[str] = None

    class Config:
        from_attributes = True


class CategoryPublic(BaseModel):
    id: int
    name: str
    slug: str

    class Config:
        from_attributes = True


class ProductPublic(BaseModel):
    id: int
    name: str
    slug: str
    price: float
    discount_percent: int
    image_url: Optional[str]
    short_desc: Optional[str]
    description: Optional[str]
    in_stock: bool
    category: CategoryPublic
    brand: BrandPublic

    class Config:
        from_attributes = True


class CartItem(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)


class OrderItemPublic(BaseModel):
    product_id: int
    quantity: int
    unit_price: float

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    items: List[CartItem]


class OrderPublic(BaseModel):
    id: int
    total: float
    status: str
    created_at: datetime
    items: List[OrderItemPublic]

    class Config:
        from_attributes = True


class MeResponse(BaseModel):
    user: UserPublic
    orders: List[OrderPublic]




