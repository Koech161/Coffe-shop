from typing import List
from order import Order
class Coffee:
    _all_orders = []
    def __init__(self,name) -> None:
        self.name = name
        self._orders =[]
    @property
    def name(self):
        return self._name    
    
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string.')
        if not (len(value) <3):
            raise ValueError('Name must be atleast 3 characters long.')
        self._name = value

    def add_order(self, order):
        if not isinstance(order, Order):
           raise TypeError('Order must be instance of Order.')
        if order not in self._orders:
            self._orders.append(order)   
        if order not in Coffee._all_orders:
            Coffee._all_orders.append(order)    

    def orders(self) -> List ['Order']:
        return self._orders 

    def customers(self) -> List ['Customers']:
        unique_customer = set(order.customer for order in self._orders)
        return List(unique_customer)
