# FILE: _whatsthestory/property_story.py 
#
# SUBJECT: Explaining the Python @property decorator 
#
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE:  2025-02-04
# SEE: https://www.programiz.com/python-programming/property

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature # implicit call of set_temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    # Getter method
    def get_temperature(self):
        print("Getting value...") # just 2c:
        return self._temperature
    
    # Setter method
    def set_temperature(self, value):
        print("Setting value...") # again just 4c'ing
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value
    
    # Creating a property object
    temperature = property(get_temperature, set_temperature)# getter & setter methods: fget, fset - we do not use fdel and doc here
    
    # When temperature is read/accessed - the functions get_* and set_* are called
    # Note: The actual temperature value is stored in the private _temperature variable. 
    # The temperature attribute is a property object which provides an interface to this private variable. 
    
    
    # The @property Decorator

    # In Python, property() is a built-in function that creates and returns a property object. The syntax of this function is:
    # 
    # property(fget=None, fset=None, fdel=None, doc=None)

    # fget is function to get value of the attribute
    # fset is function to set value of the attribute
    # fdel is function to delete the attribute
    # doc is a string (like a comment)
    
    # the line above (l. 29) is equivalent to:
    
    # temperature = property() 
    # temperature = temperature.getter(get_temperature)
    # temperature = temperature.setter(set_temperature)

    
# Create a new object
human = Celsius(37)

# Set the temperature
# human.temperature = 37

# Get the temperature attribute
print(human.temperature)

# Get the to_fahrenheit method
print(human.to_fahrenheit())

# let's have a look at the class internals:
print(human.__dict__) 


# --> human.temperature internally becomes human.__dict__['temperature'].

# human.temperature = -200

# We now do a refactoring on the *new* class Celsius, using the decorator pattern 
# SEE: https://www.programiz.com/python-programming/property
# (and renaming it to NewCelsius, not inhering)

class NewCelsius:
    def __init__(self, temperature=0):
        # when creating the object, the setter method is called automatically
        self.temperature = temperature

    def to_fahrenheit(self):
        # convert the temperature to Fahrenheit
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        # ensure the temperature does not go below absolute zero
        if value < -273.15:
            raise ValueError("Temperature below -273.15°C is not possible")
        self._temperature = value


# create an object with a valid temperature
human = NewCelsius(37)

# print the temperature in NewCelsius
print(human.temperature)

# print the temperature in Fahrenheit
print(human.to_fahrenheit())

# attempting to create an object with a temperature below -273.15°C will raise an exception
try:
    coldest_thing = NewCelsius(-300)
except ValueError as e:
    print(e)