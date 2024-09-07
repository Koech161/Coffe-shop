from order import Order
from coffee import Coffee
from typing import List
class Customer:
    _all_order = []

    def __init__(self,name):
        self.name =name
        self._order =[]
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

    def add_order(self,order):
        if not isinstance (order, Order):
            raise TypeError('Order must be instances of Order.')
        if order not in self._order:
            self._order.append(order)
        if order not in Customer._all_order:
            Customer._all_order.append(order)  

    def order(self) ->List [Order]:
        return self._order       

    def coffees(self) ->List [Coffee]:
        unique_coffee = set(order.coffee for order in self._order )
        return unique_coffee   
    
    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError('Coffee must be instances of Coffee.')
        if not isinstance(price,(float, int)):
            raise TypeError('Price must be float')
        if not (1.0 <= price <= 10.0):
            raise ValueError('price must be between 1.0 and 10.0.')
        
        order  =Order(customer = self, coffee = coffee, price = price )
        self.add_order(order)
        coffee.add_order(order)

        return order