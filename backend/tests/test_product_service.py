import pytest
from service.product_service import ProductService
from domain.product import Product

def test_create_product_success():
    service = ProductService()
    product = service.create_product(name="Laptop", price=1000)
    assert product.id is not None
    assert product.name == "Laptop"

def test_create_product_validation_error():
    service = ProductService()
    with pytest.raises(ValueError):
        service.create_product(name="", price=1000) 
