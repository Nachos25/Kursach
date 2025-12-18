from dataclasses import dataclass

@dataclass
class Category:
    id: int
    name: str

@dataclass
class Brand:
    id: int
    name: str

@dataclass
class Product:
    id: int
    name: str
    description: str
    price: float
    discount: float
    category: Category
    brand: Brand
    image_url: str

    def get_price_after_discount(self) -> float:
        return self.price * (1 - self.discount)
