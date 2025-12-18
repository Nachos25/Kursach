from dataclasses import dataclass
from domain.orders import Order

@dataclass
class Payment:
    id: int
    order: Order
    amount: float
    status: str = "PENDING"

    def process(self):
        self.status = "PAID"
