Sructured outline for domain model

1. class Customer

Attributes: customer_id, name, phone_no, email_address, order_method, loyalty_status

Methods

get_customer_info() -> Return a summary of the customers information -> (First get the customers information)

check_loyalty_status() ie "Gold", "Silver", "Bronze" -> (Then check his/her status)

set_order_method(method) ie "Mobile App" or "Cashier" -> (Then set the order method)

place_order(order) -> (Then place the order)

add_loyalty_points(points) -> Add points to the loyalty status(Finally add loyalty points)

2. class Coffee

Attributes:
coffee_id: Unique Identifier
Name(Capuccino, Expresso, Americano),
Type(cold, brewed, ), 
price, size_options(small, medium, large)

Methods

get_coffee_info() -> Returns all info of the coffee

is_available(size) -> Check if the specified size is available in the shop

get_type() -> Returns your preference of your coffee

get_price_for_size(size) -> Returns the specified price for the specified coffee

update_price(new_price) -> Updates the price of the coffee


3. class Order
 
 Attributes: 
 order_id: Unique identity for the order 
 customer_id -> Link the order customer is placing
 order_name 
 order-type
 total_price -> Total price of the order
 order_status -> Status of the order(pending // completed)

Methods

get_order_info() -> Returns the summary of the order details

add_coffee(coffee) -> Adds a coffee to the item order

calculate_total(coffee_list) -> Total price based on the coffee ordered

get_customer_id() -> Returns the customer ID associated with the order

update_status(new_status) -> Example from pending to completed


Relationships

One-to-Many

Customer and order

coffee and sizes

order to order status

Many-to-Many

order and coffe -> mutiple orders and several coffee

One-to-One

Customer to loyalty status


