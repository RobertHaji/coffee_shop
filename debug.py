from customer import Customer
from coffee import Coffee
from order import Order

# Creates customers
customer1 = Customer("Robert")
customer2 = Customer("Angel-Face")
coffee = Coffee("Latte") # Creates coffee
#Creates orders
order1 = Order(customer1, coffee, 5.0)
order2 = Order(customer2, coffee, 4.0)
# Adds orders to the coffee
coffee.add_orders(order1)
coffee.add_orders(order2)

# Create orders using the new create_order method

order1 = customer1.create_orders(coffee, 5.0)
order2 = customer2.create_orders(coffee, 4.0)









print(f"Customers who ordered {coffee.name}: {[customer.name for customer in coffee.customers()]}")
print(f"Orders for {coffee.name}: {coffee.orders()}")
print(f"Total orders for {coffee.name}: {coffee.num_orders()}")
print(f"Average price for {coffee.name}: {coffee.average_price()}")

# Test the most_aficionado method in customer.py

aficionado = Customer.most_aficionado(coffee)
if aficionado:
    print(f"The most aficionado customer for {coffee.name} is {aficionado.name}.")
else:
    print("No customers have ordered this coffee.")