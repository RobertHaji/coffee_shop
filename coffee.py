class Coffee:
    def __init__(self, name):
        self.name = name

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
        
#  Debugging with print statements
# coffee = Coffee("Capuccinno")  

# print(coffee.name)

# coffee = Coffee("Ca")

# print(coffee.name)
    
   