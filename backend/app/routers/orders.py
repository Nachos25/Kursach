from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Order, OrderItem, Product, User
from ..schemas import OrderCreate, OrderPublic
from ..security import get_current_user

router = APIRouter(prefix="/api/orders", tags=["orders"])


@router.post("", response_model=OrderPublic)
def create_order(
    order_in: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not order_in.items:
        raise HTTPException(status_code=400, detail="Кошик порожній")

    order = Order(user_id=current_user.id, total=0)
    db.add(order)
    total = 0.0
    for item in order_in.items:
        product = db.query(Product).get(item.product_id)
        if not product or not product.in_stock:
            raise HTTPException(status_code=400, detail=f"Товар недоступний: {item.product_id}")
        price = product.price * (1 - product.discount_percent / 100.0)
        total += price * item.quantity
        db.add(OrderItem(order=order, product_id=product.id, quantity=item.quantity, unit_price=price))

    order.total = round(total, 2)
    db.commit()
    db.refresh(order)
    return order


@router.get("", response_model=List[OrderPublic])
def my_orders(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return db.query(Order).filter(Order.user_id == current_user.id).order_by(Order.id.desc()).all()




