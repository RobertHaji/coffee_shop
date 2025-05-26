from order import Order
class Customer:
    def __init__(self, name):
      self.name = name

# Use property Getter to return the value of the private attribute _name
    @property

    def name (self):
       return self._name

# Use property setter 
    @name.setter

    def name (self, value):
      if isinstance (value, str) and 1 <= len(value) <= 15:
        self._name = value
      else:
        raise ValueError("Name must be the value of string between 1 and 15 characters") 
    def orders(self):
       return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
       unique_coffees = {order.coffee for order in self.orders()}
       return list(unique_coffees)
    def create_orders(self, coffee, price):
       order = Order(self, coffee, price)
       coffee.add_orders(order) #Associate the order with the coffee
       return order
    
    @classmethod

    def most_aficionado(cls, coffee):
       coffee_orders = [order for order in Order.all if order.coffee == coffee]

       #Create a dictionary to track the spending per each cutomer

       customer_spending = {}
       for order in coffee_orders:
          customer = order.customer
          # Update the spending
          customer_spending[customer] = customer_spending.get(customer, 0) + order.price

       if not customer_spending:
          return None # Means that no customer for the provided coffee

       most_spent_customer = max(customer_spending, key=customer_spending.get)
       return most_spent_customer   
         
   
#    Debugging and testing
# customer = Customer("Robert Haji")

# print(customer.name)

# # customer.name = ("VeryLongNameRobertHaji")

# # print(customer.name)



