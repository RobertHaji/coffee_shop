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
   
#    Debugging and testing
# customer = Customer("Robert Haji")

# print(customer.name)

# customer.name = ("VeryLongNameRobertHaji")

# print(customer.name)

