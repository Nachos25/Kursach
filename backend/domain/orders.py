from dataclasses import dataclass, field
from typing import List
from domain.catalog import Product
from domain.users import User

@dataclass
class OrderItem:
    product: Product
    quantity: int

    def subtotal(self) -> float:
        return self.product.get_price_after_discount() * self.quantity

@dataclass
class Order:
    id: int
    user: User
    items: List[OrderItem] = field(default_factory=list)
    status: str = "OPEN"

    def add_item(self, product: Product, quantity: int):
        self.items.append(OrderItem(product, quantity))

    def total_amount(self) -> float:
        return sum(item.subtotal() for item in self.items)
