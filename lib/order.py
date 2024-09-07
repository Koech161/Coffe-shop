from customer import Customer
from coffee import Coffee
class Order:
    def __init__(self,customer, coffee, price) -> None:
        self.customer = customer
        self.coffee =coffee
        self.price = price

    @property
    def customer(self):
        return self._customer 
       
    @customer.setter
    def customer(self,value):
        if not isinstance(value, Customer):
            raise TypeError('Customer must be instances of Customer.')
        self._customer = value

    @property 
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self,value):
        if not isinstance(value, Coffee):
            raise TypeError('Coffee must be inbstances of Coffee.')
        self._coffee = value

    @property 
    def price(self):
        return self._price   

    @price.setter
    def price(self,value):
        if not isinstance (value(float, int)):
            raise TypeError('Price must be float.')
        if not (1.0 <= value <= 10.0):
            raise ValueError('Price must be between 1.0 and 10.0.') 
        self._price = float(value)
    
    