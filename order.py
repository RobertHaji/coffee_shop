
class Order:
     all = [] #This tracks all order instances
     def __init__(self, customer, coffee, price):
      from customer import Customer
      from coffee import Coffee
      self.customer = customer
      self.coffee = coffee
      self.price = price
      Order.all.append(self) #Stores the instance

    #   Getter for the customer

      @property
      def customer(self):
        return self._customer
    #   Setter for the customer 

      @customer.setter
      def customer(self, value):
         from customer import Customer
         if isinstance (value, Customer):
            self._customer = value
         else:
            raise ValueError("Customer must be a valid Customer instance")
    #   Getter for the coffee
      @property
      def coffee(self):
         return self._coffee
    #   Setter for the coffee 
      @coffee.setter
      def coffee(self, value):
         from coffee import Coffee
         if isinstance (value, Coffee):
            self._coffee = value
         else:
            raise ValueError ("Coffee must be a valid Coffee instance")  
         
    #  Getter for the price  
     @property
     def price(self):
        return self._price
      
    #  Setter for the price  
     @price.setter
     def price(self, value):
         if isinstance(value, (int, float)) and 1.0 <= value <= 10.0:
            self._price = float(value)
         else:
            raise ValueError("Price must be a float between 1.0 and 10.0")
         
     def __repr__(self):
         return f"<Order customer={self.customer.name}, coffee={self.coffee.name}, price={self.price}>" 
    
   
    