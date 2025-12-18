from typing import List, Optional
from domain.product import Product
from datetime import datetime

class ProductService:
    def __init__(self):
        # Тимчасово використовуємо in-memory storage
        self._products: List[Product] = []
        self._next_id = 1

    def list_products(self) -> List[Product]:
        return self._products

    def get_product(self, product_id: int) -> Optional[Product]:
        return next((p for p in self._products if p.id == product_id), None)

    def create_product(self, name: str, description: str = "", price: float = 0.0, discount: float = 0.0) -> Product:
        if not name:
            raise ValueError("Name is required")
        product = Product(
            id=self._next_id,
            name=name,
            description=description,
            price=price,
            discount=discount,
        )
        self._products.append(product)
        self._next_id += 1
        return product

    def update_product(self, product_id: int, name=None, description=None, price=None, discount=None) -> Product:
        product = self.get_product(product_id)
        if not product:
            raise ValueError("Product not found")
        product.update(name, description, price, discount)
        return product

    def delete_product(self, product_id: int) -> bool:
        product = self.get_product(product_id)
        if not product:
            return False
        self._products.remove(product)
        return True
