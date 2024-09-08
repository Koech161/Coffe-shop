from lib.customer import Customer
from lib.coffee import Coffee
class Order:
    def __init__(self,customer, coffee, price: float) -> None:
        self.customer = customer
        self.coffee =coffee
        self.price = price

    @property
    def customer(self):
        return self._customer 
       
    @customer.setter
    def customer(self,value):
        if not isinstance(value, Customer):
            raise TypeError('Customer must be instance of Customer.')
        self._customer = value

    @property 
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self,value):
        if not isinstance(value, Coffee):
            raise TypeError('Coffee must be instance of Coffee.')
        self._coffee = value

    @property 
    def price(self):
        return self._price   

    @price.setter
    def price(self,value):
        if not isinstance (value,(float, int)):
            raise TypeError('Price must be a float or integer.')
        if not (1.0 <= value <= 10.0):
            raise ValueError('Price must be between 1.0 and 10.0.') 
        self._price = float(value)
    
    