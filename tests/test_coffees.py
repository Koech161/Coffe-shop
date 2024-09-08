import pytest
from lib.coffee import Coffee
from lib.customer import Customer

def test_coffee_initialization():
    coffee = Coffee(name="Latte")
    assert coffee.name == "Latte"

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee(name="L")

def test_num_orders():
    coffee = Coffee(name="Latte")
    customer = Customer(name="Alice")
    customer.create_order(coffee, 5.0)
    assert coffee.num_orders() == 0

def test_average_price():
    coffee = Coffee(name="Latte")
    customer = Customer(name="Alice")
    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 7.0)
    assert coffee.average_price() == 0
