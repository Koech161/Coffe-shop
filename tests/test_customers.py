import pytest
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

def test_customer_initialization():
    customer = Customer(name="Alice")
    assert customer.name == "Alice"

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer(name="A" * 16)

def test_create_order():
    customer = Customer(name="Alice")
    coffee = Coffee(name="Latte")
    order = customer.create_order(coffee, 5.0)
    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_coffees_method():
    customer = Customer(name="Alice")
    coffee1 = Coffee(name="Latte")
    coffee2 = Coffee(name="Espresso")
    customer.create_order(coffee1, 5.0)
    customer.create_order(coffee2, 6.0)
    assert len(customer.coffees()) == 2
