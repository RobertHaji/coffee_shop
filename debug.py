from customer import Customer
from coffee import Coffee
from order import Order

customer1 = Customer("Robert")
customer2 = Customer("Angel-Face")
coffee = Coffee("Latte")

order1 = Order(customer1, coffee, 5.0)
order2 = Order(customer2, coffee, 4.0)

coffee.add_orders(order1)
coffee.add_orders(order2)

print(f"Orders for {coffee.name}: {coffee.orders()}")
print(f"Customers who ordered {coffee.name}: {[customer.name for customer in coffee.customers()]}")