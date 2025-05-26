
class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = [] # Stores orders associated with the coffee

    @property
    # Use property Getter to return the value of the private attribute _name
    def name(self):
        return self._name 
    # Use the property setter

    @name.setter

    def name (self, value):
        if isinstance (value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError ("Name must be the value of string atleast above 3")
        
    #   The function adds an order instance to the coffee order lists 
    def add_orders(self, order):
        from order import Order
        if isinstance(order, Order): #Checks whether the provided order is a valid Order instance
            self._orders.append(order) #Adds the order to the list
        else:
            raise ValueError("The order must be a valid Order instance")
    def orders (self):
        return self._orders #Return list of orders

    def customers(self):
        unique_customers = {order.customer for order in self._orders}
        return list(unique_customers)      #Returns the unique customers as a list  


        
#  Debugging with print statements
# coffee = Coffee("Capuccinno")  

# print(coffee.name)

# coffee = Coffee("Ca")

# print(coffee.name)