from lib.customer import Customer
from lib.coffee import Coffee

alice = Customer('Alice')
bob =  Customer('Bob')

latte = Coffee('Latte')
espresso = Coffee('Espresso')

alice.create_order(latte, 2.5)

print(f'Alice coffee: {[coffee.name for coffee in alice.coffees() ]}')
print(f'Late price: {latte.average_price():.2f}')
