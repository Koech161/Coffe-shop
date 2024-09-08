from typing import List
# from lib.order import Order
from lib.coffee import Coffee

class Customer:
    _all_orders = []

    def __init__(self,name):
        self.name =name
        self._orders =[]
    @property
    def name(self):
        return self._name  
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise  TypeError('Name must be a string.')
        if not(1 <= len(value) <=15):
            raise ValueError('Name must be between 1 and 15 characters long.')
        self._name = value


    def order(self):
        return self._orders       

    def coffees(self) ->List [Coffee]:
        unique_coffee = set(order.coffee for order in self._orders )
        return list(unique_coffee )  
    
    def create_order(self, coffee, price):
        from lib.order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)
        return order
       
    @classmethod
    def most_aficionado(cls, coffee):
        customers = coffee.customers()
        if not customers:
            return None
        return max(customers, key=lambda customer: sum(order.price for order in customer.orders() if order.coffee == coffee))