# Class Automobile using dunder methods
#
# Playing with python class and trying to overload operators
# @since 2024-12-23
# @author Sven Schrodt


class Automobile:

    # constructor
    def __init__(self, type, power=100):
        self.type = type
        self.power = power

    # magic method for usage in string context
    def __str__(self):
        return f"An automobile of type: {self.type} with power of: {self.power}"

    # overload operator +
    def __add__(self, other):
        self.check_other(other)
        return round(self.power + other.power, 2)

    # overload operator -
    def __sub__(self, other):
        self.check_other(other)
        return abs(round(self.power - other.power, 2))

    def check_other(self, other):
        if not isinstance(other, Automobile):
            raise ValueError("Given value is not an instance of " + str(self.__class__))


Hugo = Automobile(type="Ford Ka", power=23.5)

Emile = Automobile(type="Ford Fiesta", power=42.23)


print(Hugo)
print(Emile)
print(Hugo + Emile)
print(Hugo - Emile)
try:
    print(Hugo + "Foo")
except ValueError as e:
    print(e)
