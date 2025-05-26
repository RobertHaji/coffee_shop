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


print(f"Customers who ordered {coffee.name}: {[customer.name for customer in coffee.customers()]}")
print(f"Orders for {coffee.name}: {coffee.orders()}")