from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Product:
    id: int
    name: str
    description: str = ""
    price: float = 0.0
    discount: float = 0.0
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def update(self, name=None, description=None, price=None, discount=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if discount is not None:
            self.discount = discount
        self.updated_at = datetime.utcnow()
