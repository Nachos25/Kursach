from domain.order import Order
from typing import Dict
from uuid import uuid4

class OrderService:
    def __init__(self):
        # Idempotency-Key -> Order
        self.idem_store: Dict[str, Order] = {}

    def create_order(self, title: str, idempotency_key: str) -> Order:
        if not idempotency_key:
            raise ValueError("idempotency_key_required")
        if idempotency_key in self.idem_store:
            return self.idem_store[idempotency_key]
        order = Order(id="ord_" + uuid4().hex[:8], title=title)
        self.idem_store[idempotency_key] = order
        return order
