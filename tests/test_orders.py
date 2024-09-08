import pytest
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

def test_order_initialization():
    customer = Customer(name="Alice")
    coffee = Coffee(name="Latte")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_validation():
    customer = Customer(name="Alice")
    coffee = Coffee(name="Latte")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5) 
