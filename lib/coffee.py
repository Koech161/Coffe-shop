
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
        if len(value) < 3:
            raise ValueError('Name must be atleast 3 characters long.')
        self._name = value
    
    def add_order(self, order) -> None:
        self._orders.append(order)
        Coffee._all_orders.append(order)

    def orders(self):
        return self._orders 

    def customers(self):
        unique_customer = set(order.customer for order in self._orders)
        return list(unique_customer)
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0.0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)